# Skill Examples

This file provides complete, working examples of skill implementations following the template pattern.

## Example 1: Simple Instruction Skill (No Additional Files)

A skill that provides guidance without needing reference files or scripts.

**Skill:** `code-review`

```markdown
---
name: code-review
description: Perform comprehensive code reviews focusing on correctness, performance, and maintainability. Use when user requests a code review, asks for feedback on code, or mentions reviewing pull requests.
---

# Code Review

## Quick Start

Paste your code and ask: "Review this for bugs and performance issues."

## Review Checklist

### Correctness
- [ ] Syntax errors
- [ ] Logical errors
- [ ] Edge cases handled
- [ ] Input validation
- [ ] Error handling

### Performance
- [ ] Time complexity analysis
- [ ] Space complexity analysis
- [ ] I/O operations optimized
- [ ] Database queries efficient
- [ ] Caching opportunities

### Maintainability
- [ ] Clear variable names
- [ ] Consistent style
- [ ] Proper comments
- [ ] DRY principles
- [ ] Test coverage

## Common Issues by Language

### Python
- Missing type hints
- Unused imports
- Inefficient list comprehensions
- Not using context managers for files

### JavaScript
- Callback hell (use async/await)
- Memory leaks in event listeners
- == vs === confusion
- Missing error handling in promises
```

**Why this works:**
- Under 100 lines
- Clear triggers in description
- Actionable checklist
- Language-specific guidance

---

## Example 2: Skill with Reference File

A skill where detailed documentation belongs in a separate file.

**Directory Structure:**
```
api-integration/
├── SKILL.md
└── REFERENCE.md
```

**SKILL.md:**
```markdown
---
name: api-integration
description: Integrate with REST APIs including authentication, pagination, and error handling. Use when user needs to connect to an API, make HTTP requests, or handle API responses.
---

# API Integration

## Quick Start

```python
import requests

response = requests.get('https://api.example.com/data')
print(response.json())
```

## Common Patterns

### Authentication

See [Authentication Methods](REFERENCE.md#authentication-methods) for detailed examples.

### Pagination

See [Pagination Strategies](REFERENCE.md#pagination-strategies).

### Error Handling

Always check status codes and handle rate limits.
```python
if response.status_code == 429:
    wait_time = int(response.headers.get('Retry-After', 60))
    time.sleep(wait_time)
    retry()
```
```

**REFERENCE.md (excerpt):**
```markdown
# API Integration Reference

## Authentication Methods

### API Keys
```python
headers = {'Authorization': f'Bearer {API_KEY}'}
```

### OAuth 2.0
```python
# See OAuth skill for complete flow
token = get_oauth_token(client_id, client_secret)
```

## Pagination Strategies

### Cursor-based
```python
cursor = None
while True:
    params = {'cursor': cursor} if cursor else {}
    response = requests.get(url, params=params)
    data = response.json()
    # Process data
    cursor = data.get('next_cursor')
    if not cursor:
        break
```

### Page-based
```python
page = 1
while True:
    response = requests.get(url, params={'page': page})
    data = response.json()
    if not data['items']:
        break
    # Process items
    page += 1
```
```

---

## Example 3: Skill with Scripts

A skill that includes executable scripts for common operations.

**Directory Structure:**
```
json-tools/
├── SKILL.md
└── scripts/
    ├── validate_json.py
    ├── format_json.py
    └── README.md
```

**SKILL.md:**
```markdown
---
name: json-tools
description: Validate, format, and transform JSON data. Use when user needs to work with JSON files, validate JSON syntax, or format JSON for readability.
---

# JSON Tools

## Quick Start

Validate a JSON file:
```bash
python scripts/validate_json.py data.json
```

Format JSON for readability:
```bash
python scripts/format_json.py input.json > output.json
```

## Available Scripts

See [scripts/README.md](scripts/README.md) for complete documentation.

## Common JSON Issues

- Trailing commas
- Missing quotes on keys
- Comments in JSON (not valid!)
- Incorrect escaping
```

**scripts/validate_json.py:**
```python
#!/usr/bin/env python3
"""
Validate JSON file syntax.

Usage:
    python validate_json.py <file.json>

Returns:
    0 if valid, 1 if invalid (with error message)
"""

import json
import sys

def validate_json(filepath: str) -> bool:
    """Validate JSON file at given path."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"✓ {filepath} is valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {filepath} is invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print(f"✗ File not found: {filepath}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_json.py <file.json>")
        sys.exit(1)
    
    valid = validate_json(sys.argv[1])
    sys.exit(0 if valid else 1)
```

**scripts/format_json.py:**
```python
#!/usr/bin/env python3
"""
Format JSON file with consistent indentation.

Usage:
    python format_json.py <input.json> [output.json]
    
    If output.json is not provided, prints to stdout.
"""

import json
import sys

def format_json(input_path: str, output_path: str = None) -> None:
    """Format JSON file with 2-space indentation."""
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    formatted = json.dumps(data, indent=2, ensure_ascii=False)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
    else:
        print(formatted)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python format_json.py <input.json> [output.json]")
        sys.exit(1)
    
    format_json(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
```

**scripts/README.md:**
```markdown
# JSON Tools Scripts

## validate_json.py

Validates JSON syntax in a file.

```bash
# Check single file
python validate_json.py data.json

# Use in shell pipeline
cat data.json | python -c "import sys,json; json.load(sys.stdin); print('Valid')"
```

## format_json.py

Formats JSON with consistent 2-space indentation.

```bash
# Format and save to new file
python format_json.py input.json output.json

# Format and print to stdout
python format_json.py input.json

# Format all JSON files in directory
for f in *.json; do
    python format_json.py "$f" "formatted_$f"
done
```
```

---

## Example 4: Complete Skill with All Components

A comprehensive skill with instructions, reference, examples, and scripts.

**Directory Structure:**
```
data-pipeline/
├── SKILL.md
├── REFERENCE.md
├── EXAMPLES.md
└── scripts/
    ├── extract.py
    ├── transform.py
    ├── load.py
    └── README.md
```

This pattern is used when:
- The skill covers a complex domain
- Multiple workflows exist
- Detailed reference material is needed
- Reusable scripts are provided
- Multiple examples help users understand

---

## Anti-Examples: What NOT to Do

### ❌ Too Vague Description

```yaml
---
name: helper
description: Helps with things.
---
```

**Problem:** Agent cannot determine when to load this skill.

### ❌ Monolithic SKILL.md

A 500-line SKILL.md with everything in one file.

**Problem:** Hard to maintain, difficult to navigate, violates progressive disclosure.

### ❌ No Examples

```markdown
# Data Analysis

This skill helps you analyze data.

Use various techniques.
```

**Problem:** User doesn't know how to start or what to expect.

### ❌ Scripts Without Documentation

```python
# process.py
def main():
    # Complex logic
    pass
```

**Problem:** No docstring, no usage instructions, unclear purpose.

### ❌ Time-Sensitive Content

```markdown
# 2024 Python Best Practices

As of Python 3.12, released in October 2023...
```

**Problem:** Will become outdated and misleading.
