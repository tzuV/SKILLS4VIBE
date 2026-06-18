---
name: repo-cleanup-audit
description: Analyze repository structure to identify modular design connections, loose scripts, and test files. Provides non-destructive cleanup recommendations with reasoning. Use when user asks to clean up repo, audit repo structure, find loose scripts, analyze modular design, or identify removable files.
---

# Repo Cleanup Audit

## Quick start

Analyze the repository to identify file connections and suggest cleanup actions.

```
1. Scan all source files and map import/dependency relationships
2. Identify core modules vs isolated/loose scripts
3. Categorize findings: KEEP, REVIEW, or REMOVE candidates
4. Provide detailed reasoning for each recommendation
```

## Workflows

### Full Repository Audit

- [ ] Run dependency analysis: grep for import statements across all source files
- [ ] Map file connections: build a graph of which files import/are imported by others
- [ ] Identify entry points: main files, CLI entry points, configuration files
- [ ] Find isolated files: files with no imports and not imported by any other file
- [ ] Detect test scripts: look for patterns like standalone scripts in root, temporary test files
- [ ] Categorize all files into: CORE, UTILITY, ISOLATED, TEST, UNKNOWN
- [ ] Generate recommendations with clear reasoning for each suggestion
- [ ] Present findings in a structured report

### Focused Analysis

If user specifies a directory or file pattern:
- [ ] Limit analysis to specified scope
- [ ] Still map external dependencies (files outside scope that depend on or are depended by scope)
- [ ] Flag files in scope that have no connections to the modular design

## Categorization Rules

### CORE (Keep - Critical)
- Imported by multiple other files
- Part of the main application flow
- Entry points (main.py, index.js, __main__.py, CLI executables)
- Configuration files referenced by other files

### UTILITY (Keep - Useful)
- Imported by at least one other file
- Helper functions/modules used elsewhere
- Shared constants or type definitions

### ISOLATED (Review - Potential Removal)
- No imports from other files in repo
- Not imported by any other file
- No clear connection to modular design
- *Reasoning*: Likely standalone scripts, experiments, or dead code

### TEST (Review - Potential Removal)
- Files matching: test_*, *_test.*, /test/, /tests/, /examples/, /scripts/
- Standalone scripts in root directory (no imports, not imported)
- Files with names: demo, example, scratch, temp, try, experiment
- *Reasoning*: Likely one-off testing scripts or temporary files

### DUPLICATE (Review - Potential Consolidation)
- Files with similar names or purposes
- Multiple versions of the same utility (utils.py, helpers.py, common.py)
- *Reasoning*: Should be consolidated into single source

## Output Format

Present findings in this structure:

```
# Repository Cleanup Audit Report

## Summary
- Total files analyzed: X
- Core files: Y
- Utility files: Z
- Isolated files: A
- Test/loose scripts: B

## Recommendations

### 🗑️ REMOVE Candidates (with reasoning)
- [ ] filename.py - Reason: isolated, no imports, not imported by others, appears to be test script
- [ ] old_script.py - Reason: duplicate functionality with newer_script.py

### 🔍 REVIEW Candidates (needs investigation)
- [ ] maybe_useful.py - Reason: imported by legacy_code.py, but legacy_code.py is deprecated

### ✅ KEEP (with reasoning)
- [ ] core_module.py - Reason: imported by 15 other files, central to application
- [ ] utils.py - Reason: imported by 5 files, shared utilities

## Connection Map
```
file1.py -> file2.py, file3.py
file2.py -> file4.py
file5.py (isolated)
```
```

## Reporting Guidelines

1. **NEVER suggest removing files you haven't analyzed**
2. **Always provide specific reasoning** for each recommendation
3. **Prioritize by impact**: Start with obvious candidates (isolated test scripts)
4. **Flag uncertainties**: Mark files as REVIEW when unsure
5. **Respect user patterns**: If user has /scripts/ dir for experiments, note this pattern
6. **Check for recent changes**: Note if isolated files were recently added (might be WIP)

## Advanced Analysis

For deeper insights, also check:
- Git history: recently modified isolated files might be work in progress
- File age: old isolated files are better removal candidates
- File size: very small files (< 20 lines) are more likely to be test scripts
- Shebang lines: standalone scripts often have #!/usr/bin/env
- TODO/FIXME comments: might indicate experimental code

See [REFERENCE.md](REFERENCE.md) for detailed analysis techniques.
