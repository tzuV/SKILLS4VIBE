# Repository Cleanup Audit - Reference

## Detailed Analysis Techniques

### Dependency Mapping Algorithm

1. **Collect all source files**
   - Python: `.py` files (exclude `__pycache__`, `.venv`, `venv`)
   - JavaScript/TypeScript: `.js`, `.ts`, `.jsx`, `.tsx`
   - Java: `.java`
   - Go: `.go`
   - Rust: `.rs`
   - Or any extension user specifies

2. **Extract imports for each language**

#### Python
```python
# Patterns to find:
import module
from module import something
from . import local_module
from .. import parent_module
```

Use regex: `(?:^|\n)\s*(?:from\s+)?([\w.]+)\s+(?:import\s+([\w,.\s]+)|import\s+([\w,.*\s]+))`

#### JavaScript/TypeScript
```javascript
// Patterns to find:
import module from 'module'
import { something } from 'module'
import * as alias from 'module'
require('module')
```

Use regex: `(?:import\s+(?:\{([^}]+)\}|\*\s+as\s+\w+\s+from\s+|([^\s]+)\s+from\s+)['"]([^'"]+)['"]|require\(['"]([^'"]+)['"]\))`

3. **Build connection graph**
   - For each file, track: `imports` (outgoing) and `imported_by` (incoming)
   - Normalize paths (handle relative imports like `.`, `..`)
   - Resolve to absolute file paths

### Identifying Modular Design

**Strong modular design indicators:**
- Clear directory structure (src/, lib/, core/, utils/)
- Files in same directory often import each other
- Entry points at top level or in specific directories (bin/, cmd/, cli/)
- Consistent import patterns

**Weak/absent modular design indicators:**
- Many files in root directory
- Inconsistent import patterns
- Files mixing concerns (business logic + utilities + tests)

### Test Script Detection Heuristics

**High confidence test scripts:**
- Path contains: `/test/`, `/tests/`, `/examples/`, `/scripts/`, `/demo/`
- Filename starts with: `test_`, `demo_`, `example_`, `scratch_`, `temp_`
- Filename ends with: `_test.py`, `_demo.py`, `_example.js`
- Filename is: `test.py`, `demo.py`, `example.js`, `main_test.go`

**Medium confidence test scripts:**
- No imports and not imported by any other file
- Contains shebang: `#!/usr/bin/env python`, `#!/usr/bin/env node`
- Very small file size (< 50 lines)
- Contains print statements for debugging
- Has hardcoded test data

**Low confidence (needs review):**
- Imported only by other suspected test files
- Has TODO or FIXME comments about being temporary
- Recent file (modified in last 30 days)

### Isolated File Detection

A file is **isolated** if:
1. It has NO imports from other files in the repository
2. It is NOT imported by any other file in the repository
3. It is NOT an entry point (main.py, package.json main, etc.)

**Exceptions to isolation rule:**
- Configuration files (config.json, .env, etc.) - these may be valid even if not imported
- Data files (JSON, CSV, etc.) - not source code
- Documentation files (README.md, etc.)
- Build configuration (package.json, pyproject.toml, etc.)

### Duplicate Detection

**Exact duplicates:**
- Same filename in different directories
- Identical file content (use hash comparison)

**Functional duplicates:**
- Similar filenames: `utils.py`, `helpers.py`, `common.py`, `utilities.py`
- Similar functionality: multiple files defining similar helper functions
- Check for: string similarity in function/variable names

### Priority Scoring for Removal Suggestions

Score each file from 0-100 (higher = more likely to be removable):

| Factor | Weight | Points |
|--------|--------|--------|
| Isolated | 30 | +30 if isolated |
| In test directory | 25 | +25 if in /test/, /tests/, etc. |
| Small file (< 20 lines) | 15 | +15 if small |
| Has shebang | 10 | +10 if has shebang |
| No imports at all | 10 | +10 if no imports |
| Old file (> 1 year) | 5 | +5 if old |
| Recent file (< 30 days) | -20 | -20 if recent (might be WIP) |
| Has TODO/FIXME | 5 | +5 if has temporary markers |
| Duplicate detected | 20 | +20 if duplicate exists |

**Scoring thresholds:**
- 70-100: Strong REMOVE candidate
- 40-69: REVIEW candidate
- 0-39: KEEP (or need more context)

## Implementation Notes

### For the Analyzing Agent

1. **Start with grep** to find all import statements
2. **Build a simple in-memory graph** of dependencies
3. **Use file system queries** to get file metadata (size, age)
4. **Check git status** if available to see recent changes
5. **Respect .gitignore** - don't analyze ignored files unless user asks

### Sample Analysis Script (Python)

See [scripts/analyze_dependencies.py](scripts/analyze_dependencies.py) for a reference implementation.

### Handling Different Languages

The skill should work across languages but can focus on:
- Python (most common for scripts)
- JavaScript/TypeScript
- Any language with clear import syntax

For unknown languages, use generic heuristics (file size, location, naming patterns).

## Example Full Analysis

```
Repository: my-project
Total files: 47

### Connection Graph
main.py -> utils.py, config.py, models/user.py
utils.py -> (none)
config.py -> (none)
models/user.py -> utils.py
scripts/test_thing.py -> (none)
temp.py -> (none)

### Categorization
- CORE: main.py (entry point, imports utils, config, models)
- CORE: models/user.py (imported by main.py)
- UTILITY: utils.py (imported by main.py and models/user.py)
- UTILITY: config.py (imported by main.py)
- ISOLATED: scripts/test_thing.py (no connections)
- ISOLATED: temp.py (no connections)

### Recommendations
REMOVE:
- temp.py (score: 85) - isolated, small (15 lines), has shebang, old (2 years)
  
REVIEW:
- scripts/test_thing.py (score: 65) - isolated but in scripts/ dir which might be intentional
  
KEEP:
- All others (connected to modular design)
```

## Common False Positives

**Don't flag as removable:**
- `__init__.py` files (even if empty, they're part of package structure)
- `conftest.py` (pytest configuration)
- `setup.py`, `pyproject.toml` (build configuration)
- `.gitignore`, `.env.example` (configuration templates)
- `Dockerfile`, `docker-compose.yml` (infrastructure)

**Be careful with:**
- Files in root that are actually used (check entry points carefully)
- Configuration files that are loaded dynamically
- Plugin architecture files
- Files loaded via reflection or dynamic imports

## Output Customization

Allow user to:
- Filter by file type/extension
- Exclude specific directories
- Adjust scoring thresholds
- Include/exclude certain patterns
- Focus on specific areas of the repo
