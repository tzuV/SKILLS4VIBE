# File Summarizer - Examples

## Quick Examples

### Example 1: Basic Folder Summary

**User Request:**
```
summarize this project
```

**Skill Response:**
```
Which folder should I scan?
```

**User Input:**
```
.
```

**Output File:** `Summarizer/summary_project_20260622_143022.md`

**Generated Summary:**
```markdown
# Summary: project

**Generated:** 2026-06-22 14:30:22  
**Source:** C:\Users\jakob\PycharmProjects\SKILLS4VIBE  
**Total Files:** 42  
**Total Size:** 2.4 MB

## 📊 Overview
This is the SKILLS4VIBE project, a collection of Mistral Vibe skills for various development tasks.

## 🗂️ Structure
```
SKILLS4VIBE/
├── .vibe/
│   └── skills/
│       ├── clean-lean-coder/
│       │   └── SKILL.md
│       ├── diagnosis/
│       │   └── SKILL.md
│       ├── file-summarizer/
│       │   ├── EXAMPLES.md
│       │   ├── REFERENCE.md
│       │   └── SKILL.md
│       └── ... (20+ other skills)
├── .gitignore
├── AGENTS.md
├── LICENSE
└── README.md
```

## 📄 File Details

### .vibe/skills/clean-lean-coder/SKILL.md
- **Path:** .vibe/skills/clean-lean-coder/SKILL.md
- **Type:** Markdown (Skill Definition)
- **Size:** 8.5 KB
- **Lines:** 245
- **Key Contents:**
  - Skill name: clean-lean-coder
  - Description: Enforce clean code principles
  - Workflows for refactoring, code review, boilerplate generation
  - Integration with other skills

### .vibe/skills/diagnosis/SKILL.md
- **Path:** .vibe/skills/diagnosis/SKILL.md
- **Type:** Markdown (Skill Definition)
- **Size:** 6.2 KB
- **Lines:** 187
- **Key Contents:**
  - Skill name: diagnosis
  - Disciplined diagnosis loop for bugs and performance
  - Reproduce, minimise, hypothesise, instrument, fix, regression-test

... (other files)

## 📈 Statistics

**File Types:**
- `.md` files: 25 (60%)
- `.py` files: 8 (19%)
- `.json` files: 5 (12%)
- `.txt` files: 4 (9%)

**Lines of Code:**
- Total lines: 12,450
- Code lines: 8,920
- Comment lines: 2,130
- Blank lines: 1,400

**Size Distribution:**
- < 1 KB: 12 files
- 1-10 KB: 22 files
- 10-100 KB: 6 files
- > 100 KB: 2 files

## 🎯 Key Findings
- Project contains 23 skill definitions
- Primary language: Markdown for skill definitions
- Well-structured with clear folder hierarchy
- Each skill has its own directory with SKILL.md
- README.md provides project overview
```

---

### Example 2: Single File Analysis

**User Request:**
```
summarize README.md
```

**Output File:** `Summarizer/summary_README_20260622_143510.md`

**Generated Summary:**
```markdown
# Summary: README.md

**Generated:** 2026-06-22 14:35:10  
**Source:** C:\Users\jakob\PycharmProjects\SKILLS4VIBE\README.md  
**Total Files:** 1  
**Total Size:** 3.2 KB

## 📊 Overview
Project README file for SKILLS4VIBE repository.

## 🗂️ Structure
Single file: README.md

## 📄 File Details

### README.md
- **Path:** README.md
- **Type:** Markdown
- **Size:** 3.2 KB
- **Lines:** 85
- **Last Modified:** 2026-06-20 10:15:00

**Sections:**
1. **Project Title** (Line 1)
   - Main heading: SKILLS4VIBE

2. **Description** (Lines 3-5)
   - Collection of Mistral Vibe skills
   - Organized by domain
   - Easy to install and use

3. **Features** (Lines 7-15)
   - 20+ skills available
   - Covers various development tasks
   - Customizable and extensible

4. **Installation** (Lines 17-25)
   - Clone repository
   - Copy to .vibe/skills/ directory
   - Restart Vibe CLI

5. **Usage** (Lines 27-40)
   - Activate with `skill:skill-name`
   - Examples for common tasks

6. **Contributing** (Lines 42-55)
   - How to add new skills
   - Pull request process

7. **License** (Lines 57-85)
   - MIT License text

## 🔗 Relationships
- Referenced in: AGENTS.md
- Mentions: skills, Mistral Vibe, CLI

## 📈 Statistics
- Words: 420
- Paragraphs: 12
- Headings: 6 (H1: 1, H2: 5)
- Links: 3
- Code blocks: 2

## 🎯 Key Findings
- Well-structured README with clear sections
- Covers all essential project documentation
- Includes practical usage examples
- Links to related documentation
```

---

### Example 3: Multi-File Code Analysis

**User Request:**
```
summarize the Python files in this project
```

**Skill Response:**
```
Which Python files should I include? (Use patterns like *.py or specific paths)
```

**User Input:**
```
**/*.py
```

**Output File:** `Summarizer/summary_python_files_20260622_144015.md`

**Generated Summary:**
```markdown
# Summary: Python Files

**Generated:** 2026-06-22 14:40:15  
**Source:** **/*.py  
**Total Files:** 8  
**Total Size:** 45.6 KB

## 📊 Overview
All Python files in the project, primarily utility scripts for skill management.

## 🗂️ Structure
```
Python Files:
├── scripts/
│   ├── install_skills.py
│   ├── update_skills.py
│   └── validate_skills.py
├── tests/
│   ├── test_skills.py
│   └── test_utils.py
├── utils/
│   ├── file_helpers.py
│   └── string_helpers.py
```

## 📄 File Details

### scripts/install_skills.py
- **Path:** scripts/install_skills.py
- **Type:** Python Script
- **Size:** 8.2 KB
- **Lines:** 210
- **Imports:** os, sys, shutil, json, pathlib
- **Functions:** 8
  - `load_skill_metadata()`
  - `copy_skill_files()`
  - `create_directory_structure()`
  - `install_skill()`
  - `uninstall_skill()`
  - `list_installed_skills()`
  - `validate_skill_structure()`
  - `main()`
- **Classes:** 1
  - `SkillInstaller`

### scripts/update_skills.py
- **Path:** scripts/update_skills.py
- **Size:** 6.1 KB
- **Lines:** 155
- **Imports:** requests, json, subprocess
- **Functions:** 5
  - `fetch_remote_skills()`
  - `compare_versions()`
  - `update_skill()`
  - `update_all_skills()`
  - `main()`

... (other Python files)

## 🔗 Relationships

**Import Graph:**
```
install_skills.py
├── imports: os, sys, shutil, json, pathlib
└── used by: update_skills.py

update_skills.py
├── imports: requests, json, subprocess
├── uses: install_skills.py (SkillInstaller)
└── used by: validate_skills.py

file_helpers.py
├── imports: os, pathlib
├── used by: install_skills.py, update_skills.py
└── functions: read_file, write_file, list_files

string_helpers.py
├── imports: re, textwrap
└── used by: file_helpers.py
```

## 📈 Statistics

**Code Metrics:**
- Total lines of code: 1,245
- Functions defined: 32
- Classes defined: 4
- Import statements: 45
- External dependencies: 8

**File Type Breakdown:**
- Script files: 3 (37.5%)
- Test files: 2 (25%)
- Utility files: 3 (37.5%)

**Complexity:**
- Average function length: 12 lines
- Maximum function length: 45 lines (install_skill)
- Average cyclomatic complexity: 3.2

## 🎯 Key Findings
- Scripts are well-organized in scripts/ directory
- Good separation of concerns between modules
- Utility functions reused across scripts
- Test coverage for core functionality
- External dependencies minimized (8 total)
```

---

### Example 4: Custom Template Usage

**User Request:**
```
summarize src/ folder using my custom template
```

**User provides custom template `quick_template.md`:**
```markdown
# Quick Summary: {{name}}

## Stats
- Files: {{file_count}}
- Total Lines: {{loc}}
- Code Lines: {{code_lines}}

## Top 5 Largest Files
{{#each largest_files}}
- {{name}}: {{lines}} lines
{{/each}}

## Dependencies
{{dependencies}}
```

**Command:**
```
skill:file-summarizer --path=src/ --template=quick_template.md
```

**Output File:** `Summarizer/summary_src_quick_20260622_144530.md`

**Generated Summary:**
```markdown
# Quick Summary: src

## Stats
- Files: 15
- Total Lines: 3,450
- Code Lines: 2,800

## Top 5 Largest Files
- main.py: 450 lines
- utils/helpers.py: 320 lines
- models/user.py: 280 lines
- api/routes.py: 250 lines
- config/settings.py: 210 lines

## Dependencies
- flask==2.3.2
- sqlalchemy==2.0.15
- requests==2.31.0
- pydantic==2.4.2
```

---

### Example 5: Filtered Summary with Exclusions

**User Request:**
```
summarize everything except tests and temporary files
```

**Command:**
```
skill:file-summarizer --path=. --exclude=*test*,*spec*,*.tmp,*.log
```

**Output File:** `Summarizer/summary_filtered_20260622_145000.md`

**Generated Summary:**
```markdown
# Summary: filtered

**Generated:** 2026-06-22 14:50:00  
**Source:** .  
**Total Files:** 34 (excluded 8 test/temp files)  
**Total Size:** 1.8 MB

## 📊 Overview
Project files excluding tests, specs, temporary, and log files.

## 🗂️ Structure
```
SKILLS4VIBE/
├── .vibe/
│   └── skills/
│       ├── clean-lean-coder/
│       │   └── SKILL.md
│       ├── diagnosis/
│       │   └── SKILL.md
│       └── ...
├── AGENTS.md
├── LICENSE
└── README.md
```

## 📁 Excluded Files
- tests/test_skills.py
- tests/test_utils.py
- logs/debug.log
- temp/temp_file.tmp

## 📄 File Details
... (details of included files)

## 🎯 Key Findings
- 34 production files analyzed
- 8 files excluded by filter
- Clean separation between source and test files
```

---

### Example 6: Incremental Update

**User Request (Day 1):**
```
summarize the project
```

**First Summary:** `Summarizer/summary_project_20260621_100000.md`
- 40 files analyzed
- Total size: 2.2 MB

**User Request (Day 2, after adding new files):**
```
summarize the project again
```

**Skill detects changes:**
- 2 new files added
- 3 files modified
- 0 files deleted

**Output File:** `Summarizer/summary_project_20260622_100000.md`

**Generated Summary (Diff Mode):**
```markdown
# Summary: project (Updated)

**Generated:** 2026-06-22 10:00:00  
**Source:** .  
**Previous Summary:** [2026-06-21 10:00:00](Summarizer/summary_project_20260621_100000.md)  
**Changes Since:** 24 hours ago  

## 📊 Changes

### New Files (2)
1. **scripts/new_script.py**
   - Size: 3.2 KB
   - Lines: 85
   - Purpose: Automated skill validation

2. **docs/api.md**
   - Size: 5.1 KB
   - Lines: 140
   - Purpose: API documentation

### Modified Files (3)
1. **README.md**
   - Previous: 85 lines, 3.2 KB
   - Current: 92 lines, 3.5 KB
   - Changes: Added installation troubleshooting section

2. **utils/file_helpers.py**
   - Previous: 120 lines
   - Current: 135 lines
   - Changes: Added new helper functions

3. **AGENTS.md**
   - Previous: 45 lines
   - Current: 50 lines
   - Changes: Updated security rules

### Deleted Files (0)
None

## 📈 Updated Statistics
- Total files: 42 (+2)
- Total size: 2.5 MB (+0.3 MB)
- Total lines: 13,200 (+750)

## 🎯 Summary
- Project is actively maintained
- New functionality added (validation script)
- Documentation improved (API docs, troubleshooting)
- Codebase growing steadily
```

---

### Example 7: Codebase with Dependency Analysis

**User Request:**
```
summarize src/ folder with dependency map
```

**Command:**
```
skill:file-summarizer --path=src/ --code-analysis --dependency-map
```

**Output File:** `Summarizer/summary_src_dependencies_20260622_150000.md`

**Generated Summary:**
```markdown
# Summary: src with Dependencies

**Generated:** 2026-06-22 15:00:00  
**Source:** src/  
**Total Files:** 15  
**Total Size:** 45.6 KB

## 📊 Overview
Source code with full dependency analysis.

## 🗂️ Structure
... (structure tree)

## 🔗 Dependency Graph

```
main.py
├── imports: flask, config, utils
│   ├── flask: Flask, request, jsonify
│   ├── config: settings, database
│   └── utils: helpers, validators
├── used by: routes.py
└── uses: models/, services/

routes.py
├── imports: flask, main, services
│   ├── flask: Blueprint, render_template
│   ├── main: app
│   └── services: user_service, auth_service
└── used by: (entry point)

models/user.py
├── imports: sqlalchemy, config
│   ├── sqlalchemy: Column, Integer, String, Relationship
│   └── config: database
└── used by: services/user_service.py, routes.py

services/user_service.py
├── imports: models, utils
│   ├── models: User, db_session
│   └── utils: logger, validators
└── used by: routes.py

config/settings.py
├── imports: os, dotenv
│   ├── os: environ, path
│   └── dotenv: load_dotenv
└── used by: main.py, models/, services/
```

## 📦 External Dependencies

**Production:**
- flask==2.3.2 (web framework)
- sqlalchemy==2.0.15 (ORM)
- python-dotenv==1.0.0 (environment)
- pydantic==2.4.2 (data validation)

**Development:**
- pytest==7.4.0 (testing)
- black==23.7.0 (formatting)
- flake8==6.1.0 (linting)

**Version Status:**
- ✅ All dependencies up to date
- ⚠️ flask has newer version available (2.3.3)
- ❌ No security vulnerabilities detected

## 📊 Code Metrics

**By File:**
| File | LOC | Functions | Classes | Complexity |
|------|-----|-----------|---------|------------|
| main.py | 450 | 12 | 1 | 15 |
| routes.py | 250 | 8 | 0 | 10 |
| models/user.py | 280 | 5 | 2 | 8 |
| services/user_service.py | 320 | 10 | 0 | 12 |

**Totals:**
- Lines of code: 3,450
- Functions: 48
- Classes: 5
- Average complexity: 8.4
- Max complexity: 15 (main.py)

## 🎯 Key Findings
- Well-structured with clear separation of concerns
- Dependency graph shows good modularity
- No circular dependencies detected
- External dependencies well-managed
- Test coverage: 85% (estimated)
```

---

## Template Examples

### Minimal Template
```markdown
# {{name}}

Files: {{file_count}}
Size: {{total_size}}
```

### Code-Focused Template
```markdown
# Code Analysis: {{name}}

## Metrics
- LOC: {{loc}}
- Functions: {{functions}}
- Classes: {{classes}}
- Complexity: {{code_complexity}}

## Imports
{{imports}}

## Exports
{{exports}}
```

### Documentation Template
```markdown
# Documentation Summary: {{name}}

## Overview
{{#if description}}{{description}}{{/if}}

## Sections
{{#each sections}}
### {{title}}
{{content}}
{{/each}}
```

### Comparison Template
```markdown
# Comparison: {{name}}

## Before vs After
| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Files | {{prev_file_count}} | {{file_count}} | {{file_change}} |
| Size | {{prev_total_size}} | {{total_size}} | {{size_change}} |
| LOC | {{prev_loc}} | {{loc}} | {{loc_change}} |
```
