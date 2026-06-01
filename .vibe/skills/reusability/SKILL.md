---
name: reusability
description: Consolidate all functions from Python files in a project into a single utils.py file. Ensure all functions have docstrings, remove redundant duplicates, and update other files to import from utils.py.
disable-model-invocation: true
---

Consolidate all Python functions in this project into a utils.py file.
1. Scan all Python files in the project directory.
2. Extract all functions, including their code and docstrings.
3. Detect and remove duplicate functions, keeping the first occurrence.
4. Move all unique functions into utils.py, ensuring each has a descriptive docstring.
5. Update all other files to import functions from utils.py instead of defining them locally.
6. Verify the project still runs correctly after refactoring.