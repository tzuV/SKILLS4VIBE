#!/usr/bin/env python3
"""
Validate that a skill directory follows the recommended structure.

Usage:
    python validate_skill.py <skill-directory>

Checks:
    - Required SKILL.md exists
    - SKILL.md has valid frontmatter (name, description)
    - SKILL.md is under 100 lines (recommendation)
    - Description follows format (two sentences, includes triggers)
    - Optional files (REFERENCE.md, EXAMPLES.md) exist if referenced
    - Scripts have docstrings

Returns:
    0 if valid, 1 if invalid (with error messages)
"""

import os
import re
import sys
from pathlib import Path


def check_skill_directory(skill_path: str) -> tuple[bool, list[str]]:
    """
    Validate a skill directory structure.
    
    Args:
        skill_path: Path to the skill directory
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    skill_path = Path(skill_path)
    
    # Check directory exists
    if not skill_path.is_dir():
        errors.append(f"[X] Directory not found: {skill_path}")
        return False, errors
    
    # Check required SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"[X] Missing required file: {skill_md}")
        return False, errors
    
    # Read SKILL.md content
    with open(skill_md, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()
    
    # Check frontmatter exists
    frontmatter_pattern = r'^---\s*\n(.*?)\n---'
    frontmatter_match = re.search(frontmatter_pattern, content, re.DOTALL)
    if not frontmatter_match:
        errors.append("[X] SKILL.md missing frontmatter (---)")
        return False, errors
    
    frontmatter = frontmatter_match.group(1)
    
    # Check required fields in frontmatter
    name_pattern = r'^name:\s*(.+)$'
    desc_pattern = r'^description:\s*(.+)$'
    
    name_match = re.search(name_pattern, frontmatter, re.MULTILINE)
    desc_match = re.search(desc_pattern, frontmatter, re.MULTILINE)
    
    if not name_match:
        errors.append("[X] Frontmatter missing 'name' field")
    elif len(name_match.group(1).strip()) > 64:
        errors.append("[X] Name exceeds 64 characters")
    
    if not desc_match:
        errors.append("[X] Frontmatter missing 'description' field")
    else:
        description = desc_match.group(1).strip()
        if len(description) > 1024:
            errors.append("[X] Description exceeds 1024 characters")
        
        # Check description has two sentences (at least one period)
        if '.' not in description:
            errors.append("[X] Description should have at least one period (two sentences recommended)")
        
        # Check description includes triggers
        if 'use when' not in description.lower():
            errors.append("[X] Description should include 'Use when' for discoverability")
    
    # Check SKILL.md length recommendation
    if len(lines) > 100:
        errors.append(f"[!] SKILL.md has {len(lines)} lines (recommend under 100)")
    
    # Check for referenced files that don't exist
    ref_pattern = r'\[(REFERENCE|EXAMPLES)\.md\]'
    for match in re.finditer(ref_pattern, content):
        ref_file = skill_path / f"{match.group(1)}.md"
        if not ref_file.is_file():
            errors.append(f"[X] SKILL.md references {ref_file.name} but file doesn't exist")
    
    # Check scripts directory
    scripts_dir = skill_path / "scripts"
    if scripts_dir.is_dir():
        for script in scripts_dir.glob("*.py"):
            with open(script, 'r', encoding='utf-8') as f:
                script_content = f.read()
            
            # Check for docstring (either """ or ''')
            docstring_pattern = r'^(?:["\']{3}|\"\"\"|\'\'\').*?(?:["\']{3}|\"\"\"|\'\'\')'
            if not re.search(docstring_pattern, script_content, re.MULTILINE | re.DOTALL):
                errors.append(f"[X] Script missing docstring: {script.name}")
    
    # Check optional files
    optional_files = ["REFERENCE.md", "EXAMPLES.md"]
    for opt_file in optional_files:
        file_path = skill_path / opt_file
        if file_path.is_file():
            with open(file_path, 'r', encoding='utf-8') as f:
                opt_content = f.read()
                if len(opt_content) < 10:
                    errors.append(f"[!] {opt_file} seems too short (only {len(opt_content)} bytes)")
    
    return len(errors) == 0, errors


def print_results(skill_path: str, is_valid: bool, errors: list[str]) -> None:
    """Print validation results."""
    print(f"\nValidating: {skill_path}")
    print("=" * 60)
    
    if is_valid:
        print("[OK] Skill structure is valid!")
    else:
        print("[FAIL] Skill has validation errors:\n")
        for error in errors:
            print(f"  {error}")
    
    print("=" * 60)


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <skill-directory>")
        print(f"\nExample: {sys.argv[0]} ../write-a-skill")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    is_valid, errors = check_skill_directory(skill_path)
    print_results(skill_path, is_valid, errors)
    
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
