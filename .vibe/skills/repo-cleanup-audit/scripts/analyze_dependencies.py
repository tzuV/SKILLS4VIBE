#!/usr/bin/env python3
"""
Repository Cleanup Audit - Dependency Analyzer

This script analyzes a repository to identify:
- File connections and import relationships
- Isolated files (no imports, not imported)
- Potential test/loose scripts
- Modular design patterns

Usage:
    python analyze_dependencies.py [directory] [options]

Options:
    --ext EXT1,EXT2    Comma-separated list of file extensions to analyze (default: py,js,ts)
    --exclude DIR      Comma-separated list of directories to exclude
    --output FILE      Output file for report (default: stdout)
    --json             Output in JSON format
"""

import os
import sys
import re
import json
import hashlib
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict


@dataclass
class FileInfo:
    path: str
    size: int
    mtime: float
    is_entry_point: bool = False
    imports: Set[str] = field(default_factory=set)
    imported_by: Set[str] = field(default_factory=set)
    has_shebang: bool = False
    line_count: int = 0
    content_hash: str = ""
    is_test_pattern: bool = False
    has_todo: bool = False


@dataclass
class Recommendation:
    file_path: str
    category: str  # REMOVE, REVIEW, KEEP
    score: int
    reasons: List[str]


class DependencyAnalyzer:
    # Regex patterns for different languages
    PYTHON_IMPORT_PATTERN = re.compile(
        r'(?:^|\n)\s*(?:from\s+)?([\w.]+)\s+(?:import\s+([\w,.\s]+)|import\s+([\w,.*\s]+))',
        re.MULTILINE
    )
    
    JS_IMPORT_PATTERN = re.compile(
        r'(?:import\s+(?:\{([^}]+)\}|\*\s+as\s+\w+\s+from\s+|([^\s]+)\s+from\s+)["']([^"'\s]+)["']|require\(["']([^"']+)["' ]',
        re.MULTILINE
    )
    
    SHEBANG_PATTERN = re.compile(r'^#!.*\n', re.MULTILINE)
    TODO_PATTERN = re.compile(r'(?:TODO|FIXME|XXX|HACK|NOTE)', re.IGNORECASE)
    
    # Test file patterns
    TEST_DIR_PATTERNS = ['test', 'tests', 'testing', 'example', 'examples', 
                         'demo', 'demos', 'script', 'scripts', 'scratch', 'temp']
    TEST_FILE_PATTERNS = [
        r'^test_', r'_test\.', r'^demo_', r'_demo\.', r'^example_',
        r'\.spec\.', r'^scratch_', r'^temp_', r'^-test', r'test\.py$',
        r'demo\.py$', r'example\.js$'
    ]
    
    # Entry point patterns
    ENTRY_POINT_PATTERNS = [
        'main.py', 'index.py', 'app.py', '__main__.py',
        'index.js', 'app.js', 'main.js', 'server.js',
        'cli.py', 'command.py', 'run.py'
    ]
    
    # Files to never suggest removing
    PROTECTED_FILES = [
        '__init__.py', 'conftest.py', 'setup.py', 'pyproject.toml',
        'package.json', 'requirements.txt', 'Dockerfile',
        'docker-compose.yml', '.gitignore', '.env', '.env.example',
        'README.md', 'LICENSE', 'Makefile', 'setup.cfg'
    ]
    
    # Extensions for different languages
    LANGUAGE_EXTENSIONS = {
        'python': ['.py'],
        'javascript': ['.js', '.jsx', '.mjs', '.cjs'],
        'typescript': ['.ts', '.tsx'],
        'java': ['.java'],
        'go': ['.go'],
        'rust': ['.rs'],
        'ruby': ['.rb'],
        'php': ['.php'],
    }
    
    def __init__(self, root_dir: str, extensions: List[str] = None, exclude_dirs: List[str] = None):
        self.root_dir = Path(root_dir).resolve()
        self.extensions = extensions or ['py', 'js', 'ts']
        self.exclude_dirs = exclude_dirs or ['node_modules', '.git', '__pycache__', '.venv', 'venv', 'dist', 'build']
        self.files: Dict[str, FileInfo] = {}
        self.duplicates: Dict[str, List[str]] = defaultdict(list)
    
    def should_skip_dir(self, dir_path: Path) -> bool:
        """Check if directory should be excluded from analysis."""
        for exclude in self.exclude_dirs:
            if exclude in str(dir_path):
                return True
        return False
    
    def has_extension(self, filepath: Path) -> bool:
        """Check if file has one of the target extensions."""
        ext = filepath.suffix.lower()
        return ext.startswith(f'.{self.extensions}') or ext[1:] in self.extensions
    
    def is_protected(self, filename: str) -> bool:
        """Check if file is in protected list."""
        return any(pattern in filename for pattern in self.PROTECTED_FILES)
    
    def is_test_pattern(self, filepath: Path) -> bool:
        """Check if file path matches test patterns."""
        filename = filepath.name
        path_str = str(filepath).lower()
        
        # Check directory patterns
        for pattern in self.TEST_DIR_PATTERNS:
            if f'/{pattern}/' in path_str or path_str.endswith(f'/{pattern}'):
                return True
        
        # Check filename patterns
        for pattern in self.TEST_FILE_PATTERNS:
            if re.search(pattern, filename, re.IGNORECASE):
                return True
        
        return False
    
    def is_entry_point(self, filepath: Path) -> bool:
        """Check if file is likely an entry point."""
        filename = filepath.name.lower()
        return any(pattern == filename for pattern in self.ENTRY_POINT_PATTERNS)
    
    def extract_imports_python(self, content: str) -> Set[str]:
        """Extract imports from Python code."""
        imports = set()
        for match in self.PYTHON_IMPORT_PATTERN.finditer(content):
            module = match.group(1)
            if module and module not in ('', '.', '..'):
                imports.add(module)
            if match.group(2):
                parts = match.group(2).replace(' ', '').split(',')
                for part in parts:
                    if part and part != module:
                        imports.add(part)
            if match.group(3):
                parts = match.group(3).replace(' ', '').split(',')
                for part in parts:
                    if part:
                        imports.add(part)
        return imports
    
    def extract_imports_javascript(self, content: str) -> Set[str]:
        """Extract imports from JavaScript/TypeScript code."""
        imports = set()
        for match in self.JS_IMPORT_PATTERN.finditer(content):
            for i in range(1, 5):
                if match.group(i):
                    imports.add(match.group(i))
        return imports
    
    def extract_imports(self, filepath: Path, content: str) -> Set[str]:
        """Extract imports based on file extension."""
        ext = filepath.suffix.lower()
        if ext == '.py':
            return self.extract_imports_python(content)
        elif ext in ['.js', '.jsx', '.mjs', '.cjs', '.ts', '.tsx']:
            return self.extract_imports_javascript(content)
        else:
            # Generic fallback - look for common patterns
            return set()
    
    def resolve_import(self, import_name: str, source_file: Path) -> Optional[str]:
        """Try to resolve an import to a file path."""
        source_dir = source_file.parent
        
        # Handle relative imports
        if import_name.startswith('.'):
            parts = import_name.split('.')
            current = source_dir
            for part in parts:
                if part == '':
                    continue
                elif part == '..':
                    current = current.parent
                else:
                    current = current / part
            
            # Check for file or directory
            possible_file = current.with_suffix('.py')
            if possible_file.exists():
                return str(possible_file.relative_to(self.root_dir))
            
            possible_dir = current / '__init__.py'
            if possible_dir.exists():
                return str(possible_dir.relative_to(self.root_dir))
            
            return None
        
        # Handle absolute imports - try to find in repo
        # This is a simplified version - real resolution is complex
        possible_paths = [
            self.root_dir / import_name,
            self.root_dir / import_name / '__init__.py',
        ]
        
        for p in possible_paths:
            if p.exists():
                return str(p.relative_to(self.root_dir))
        
        return None
    
    def scan_files(self):
        """Scan all files in the repository."""
        for root, dirs, files in os.walk(self.root_dir):
            # Remove excluded directories from the search
            dirs[:] = [d for d in dirs if not self.should_skip_dir(Path(root) / d)]
            
            for filename in files:
                filepath = Path(root) / filename
                if not self.has_extension(filepath):
                    continue
                
                rel_path = str(filepath.relative_to(self.root_dir))
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    stat = filepath.stat()
                    line_count = len(content.splitlines())
                    
                    # Calculate hash for duplicate detection
                    content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
                    
                    info = FileInfo(
                        path=rel_path,
                        size=stat.st_size,
                        mtime=stat.st_mtime,
                        is_entry_point=self.is_entry_point(filepath),
                        has_shebang=bool(self.SHEBANG_PATTERN.search(content)),
                        line_count=line_count,
                        content_hash=content_hash,
                        is_test_pattern=self.is_test_pattern(filepath),
                        has_todo=bool(self.TODO_PATTERN.search(content))
                    )
                    
                    # Extract raw imports
                    raw_imports = self.extract_imports(filepath, content)
                    info.imports = raw_imports
                    
                    self.files[rel_path] = info
                    
                    # Track duplicates
                    self.duplicates[content_hash].append(rel_path)
                    
                except (IOError, UnicodeDecodeError) as e:
                    print(f"Warning: Could not read {filepath}: {e}")
                    continue
    
    def resolve_all_imports(self):
        """Resolve all imports to build the dependency graph."""
        for rel_path, info in self.files.items():
            resolved = set()
            for imp in info.imports:
                resolved_path = self.resolve_import(imp, Path(self.root_dir) / rel_path)
                if resolved_path and resolved_path in self.files:
                    resolved.add(resolved_path)
                    # Update the imported_by relationship
                    self.files[resolved_path].imported_by.add(rel_path)
            info.imports = resolved
    
    def calculate_score(self, rel_path: str) -> Tuple[int, List[str]]:
        """Calculate a score for how likely a file is to be removable."""
        info = self.files[rel_path]
        score = 0
        reasons = []
        
        # Isolated check
        is_isolated = len(info.imports) == 0 and len(info.imported_by) == 0
        if is_isolated:
            score += 30
            reasons.append("isolated (no imports, not imported)")
        
        # Test pattern
        if info.is_test_pattern:
            score += 25
            reasons.append("matches test file pattern")
        
        # Small file
        if info.line_count < 20:
            score += 15
            reasons.append(f"small file ({info.line_count} lines)")
        elif info.line_count < 50:
            score += 10
            reasons.append(f"small file ({info.line_count} lines)")
        
        # Has shebang
        if info.has_shebang:
            score += 10
            reasons.append("has shebang line")
        
        # No imports at all
        if len(info.imports) == 0:
            score += 10
            reasons.append("has no imports")
        
        # Old file (> 1 year)
        # Note: This is simplified - would need current time
        # For now, just check if it's old relative to other files
        if info.mtime < os.path.getmtime(self.root_dir) - (365 * 24 * 60 * 60):
            score += 5
            reasons.append("old file (> 1 year)")
        
        # Recent file (< 30 days) - REDUCES score
        if info.mtime > os.path.getmtime(self.root_dir) - (30 * 24 * 60 * 60):
            score -= 20
            reasons.append("recent file (< 30 days) - might be WIP")
        
        # Has TODO/FIXME
        if info.has_todo:
            score += 5
            reasons.append("contains TODO/FIXME markers")
        
        # Duplicate
        if len(self.duplicates[info.content_hash]) > 1:
            score += 20
            reasons.append(f"duplicate content ({len(self.duplicates[info.content_hash])} copies)")
        
        # Protected files - always reduce score to 0
        if self.is_protected(rel_path):
            score = 0
            reasons = ["protected file"]
        
        # Entry points - reduce score
        if info.is_entry_point:
            score = max(0, score - 50)
            reasons.append("entry point")
        
        return score, reasons
    
    def categorize_file(self, rel_path: str) -> str:
        """Categorize a file based on its connections."""
        info = self.files[rel_path]
        
        if self.is_protected(rel_path):
            return "PROTECTED"
        
        is_isolated = len(info.imports) == 0 and len(info.imported_by) == 0
        
        # Entry points are always CORE
        if info.is_entry_point:
            return "CORE"
        
        # Imported by many -> CORE
        if len(info.imported_by) >= 3:
            return "CORE"
        
        # Imported by some -> UTILITY
        if len(info.imported_by) >= 1:
            return "UTILITY"
        
        # Test pattern files
        if info.is_test_pattern:
            return "TEST"
        
        # Isolated
        if is_isolated:
            return "ISOLATED"
        
        return "UNKNOWN"
    
    def generate_recommendations(self) -> List[Recommendation]:
        """Generate cleanup recommendations."""
        recommendations = []
        
        for rel_path, info in sorted(self.files.items()):
            score, reasons = self.calculate_score(rel_path)
            category = self.categorize_file(rel_path)
            
            # Determine recommendation category
            if category == "PROTECTED":
                rec_category = "KEEP"
            elif category == "CORE":
                rec_category = "KEEP"
            elif category == "UTILITY":
                rec_category = "KEEP"
            elif category == "TEST":
                if score >= 70:
                    rec_category = "REMOVE"
                elif score >= 40:
                    rec_category = "REVIEW"
                else:
                    rec_category = "KEEP"
            elif category == "ISOLATED":
                if score >= 70:
                    rec_category = "REMOVE"
                elif score >= 40:
                    rec_category = "REVIEW"
                else:
                    rec_category = "KEEP"
            else:
                if score >= 70:
                    rec_category = "REMOVE"
                elif score >= 40:
                    rec_category = "REVIEW"
                else:
                    rec_category = "KEEP"
            
            recommendations.append(Recommendation(
                file_path=rel_path,
                category=rec_category,
                score=score,
                reasons=reasons
            ))
        
        # Sort by score (highest first for REMOVE candidates)
        recommendations.sort(key=lambda r: r.score, reverse=True)
        return recommendations
    
    def generate_report(self, recommendations: List[Recommendation]) -> str:
        """Generate a human-readable report."""
        lines = []
        lines.append("# Repository Cleanup Audit Report")
        lines.append("")
        lines.append(f"Repository: {self.root_dir}")
        lines.append(f"Files analyzed: {len(self.files)}")
        lines.append("")
        
        # Summary
        categories = defaultdict(int)
        for rec in recommendations:
            categories[rec.category] += 1
        
        lines.append("## Summary")
        for cat, count in sorted(categories.items()):
            lines.append(f"- {cat}: {count}")
        lines.append("")
        
        # Connection map
        lines.append("## Connection Map")
        lines.append("")
        for rel_path, info in sorted(self.files.items()):
            if info.imports:
                imports_str = ", ".join(sorted(info.imports))
                lines.append(f"{rel_path} -> {imports_str}")
            elif info.imported_by:
                imported_str = ", ".join(sorted(info.imported_by))
                lines.append(f"{rel_path} <- {imported_str}")
            else:
                lines.append(f"{rel_path} (isolated)")
        lines.append("")
        
        # Duplicates
        if any(len(v) > 1 for v in self.duplicates.values()):
            lines.append("## Duplicate Files")
            lines.append("")
            for hash_val, paths in sorted(self.duplicates.items()):
                if len(paths) > 1:
                    lines.append(f"- {', '.join(paths)}")
            lines.append("")
        
        # Recommendations
        lines.append("## Recommendations")
        lines.append("")
        
        # Group by category
        remove_recs = [r for r in recommendations if r.category == "REMOVE"]
        review_recs = [r for r in recommendations if r.category == "REVIEW"]
        keep_recs = [r for r in recommendations if r.category == "KEEP"]
        
        if remove_recs:
            lines.append("### 🗑️ REMOVE Candidates")
            lines.append("")
            for rec in remove_recs:
                reasons_str = ", ".join(rec.reasons)
                lines.append(f"- [ ] {rec.file_path} (score: {rec.score}) - Reason: {reasons_str}")
            lines.append("")
        
        if review_recs:
            lines.append("### 🔍 REVIEW Candidates")
            lines.append("")
            for rec in review_recs:
                reasons_str = ", ".join(rec.reasons)
                lines.append(f"- [ ] {rec.file_path} (score: {rec.score}) - Reason: {reasons_str}")
            lines.append("")
        
        if keep_recs:
            lines.append("### ✅ KEEP")
            lines.append("")
            for rec in keep_recs:
                reasons_str = ", ".join(rec.reasons)
                cat = self.categorize_file(rec.file_path)
                lines.append(f"- [x] {rec.file_path} ({cat}) - Reason: {reasons_str}")
            lines.append("")
        
        return "\n".join(lines)
    
    def generate_json_report(self, recommendations: List[Recommendation]) -> dict:
        """Generate a JSON report."""
        return {
            "repository": str(self.root_dir),
            "files_analyzed": len(self.files),
            "summary": {
                "REMOVE": len([r for r in recommendations if r.category == "REMOVE"]),
                "REVIEW": len([r for r in recommendations if r.category == "REVIEW"]),
                "KEEP": len([r for r in recommendations if r.category == "KEEP"]),
            },
            "duplicates": {hash_val: paths for hash_val, paths in self.duplicates.items() if len(paths) > 1},
            "recommendations": [
                {
                    "file": rec.file_path,
                    "category": rec.category,
                    "score": rec.score,
                    "reasons": rec.reasons
                }
                for rec in recommendations
            ]
        }
    
    def analyze(self, output_format: str = "text") -> str:
        """Run full analysis."""
        print(f"Analyzing repository: {self.root_dir}", file=sys.stderr)
        
        self.scan_files()
        print(f"Found {len(self.files)} files to analyze", file=sys.stderr)
        
        self.resolve_all_imports()
        print("Built dependency graph", file=sys.stderr)
        
        recommendations = self.generate_recommendations()
        
        if output_format == "json":
            return json.dumps(self.generate_json_report(recommendations), indent=2)
        else:
            return self.generate_report(recommendations)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze repository dependencies and suggest cleanup')
    parser.add_argument('directory', nargs='?', default='.', help='Directory to analyze')
    parser.add_argument('--ext', default='py,js,ts', help='File extensions to analyze')
    parser.add_argument('--exclude', default='', help='Directories to exclude (comma-separated)')
    parser.add_argument('--output', help='Output file')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    
    args = parser.parse_args()
    
    extensions = args.ext.split(',')
    exclude_dirs = args.exclude.split(',') if args.exclude else []
    
    analyzer = DependencyAnalyzer(
        root_dir=args.directory,
        extensions=extensions,
        exclude_dirs=exclude_dirs + ['node_modules', '.git', '__pycache__', '.venv', 'venv']
    )
    
    output_format = "json" if args.json else "text"
    report = analyzer.analyze(output_format=output_format)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == '__main__':
    main()
