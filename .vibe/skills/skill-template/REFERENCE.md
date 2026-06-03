# Skill Reference Documentation

This document provides detailed specifications for creating Vibe skills.

## SKILL.md Specification

### Frontmatter (Required)

```yaml
---
name: skill-name
description: Brief description of capability. Use when [specific triggers].
---
```

**Field Requirements:**

| Field | Max Length | Required | Format |
|-------|------------|----------|--------|
| name | 64 chars | Yes | lowercase, hyphens only |
| description | 1024 chars | Yes | Third person, two sentences |

### Description Guidelines

The description is **critical** for skill discovery. Your agent reads ONLY this text when deciding which skill to load.

**Structure:**
1. First sentence: What the skill does (capability)
2. Second sentence: When to trigger it (use cases, keywords, contexts)

**Good Examples:**
```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.

Analyze Python code for performance bottlenecks and suggest optimizations. Use when user asks to optimize, profile, or speed up Python code.
```

**Bad Examples:**
```
Helps with documents.  # Too vague

A skill for Python.     # No triggers specified
```

### Content Structure

```markdown
# Skill Name

## Quick start

[Minimal working example - user can copy/paste and it works]

## Workflows

[Step-by-step processes with checklists for complex tasks]

### Workflow 1: [Name]
- Step 1
- Step 2
- Step 3

## Advanced features

[Link to separate files or detailed explanations]

## Troubleshooting

[Common issues and solutions]
```

**Best Practices:**
- Keep SKILL.md under 100 lines
- Use concrete examples
- Link to REFERENCE.md for details
- Include checklists for multi-step workflows
- Use consistent terminology throughout

## REFERENCE.md

Use for:
- Detailed technical specifications
- API documentation
- Configuration options
- Advanced use cases
- Architecture decisions

**When to create:** When SKILL.md would exceed 100 lines or when detailed reference material is needed.

## EXAMPLES.md

Use for:
- Complete working examples
- Before/after comparisons
- Multiple approaches to the same problem
- Test cases

**Structure:**
```markdown
# Examples

## Example 1: [Brief description]

**Input:**
```python
# Code or command
```

**Output:**
```
Expected result
```

**Explanation:**
What happened and why.
```

## Scripts Directory

Use for:
- Deterministic operations (validation, formatting, transformation)
- Code that would be generated repeatedly
- Error handling that needs to be explicit
- Resource files (templates, schemas, configs)

**When to create:**
- Operation is deterministic (same input always produces same output)
- Same code would be regenerated in multiple sessions
- Errors need explicit, consistent handling

**File Structure:**
```
scripts/
├── main.py          # Primary script
├── utils/           # Helper functions
│   └── validation.py
├── templates/       # Template files
│   └── config.json
└── README.md        # Script documentation
```

**Script Requirements:**
- Include shebang if executable: `#!/usr/bin/env python3`
- Add docstrings explaining purpose and usage
- Handle errors gracefully with clear messages
- Include type hints for Python scripts
- Add a README.md if multiple scripts exist

## File Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Skill directory | lowercase, hyphen-separated | `data-analysis` |
| Main file | SKILL.md | `SKILL.md` |
| Reference | REFERENCE.md | `REFERENCE.md` |
| Examples | EXAMPLES.md | `EXAMPLES.md` |
| Scripts | lowercase, underscore or hyphen | `validate.py`, `data-processor.js` |

## Content Guidelines

### What NOT to Include

- Time-sensitive information (dates, versions that will change)
- User-specific paths or configurations
- Temporary debugging code
- Large binary files or datasets
- Duplicated content (link instead)

### What TO Include

- Clear, actionable instructions
- Concrete examples with expected outputs
- Common pitfalls and how to avoid them
- Cross-references to related skills
- Progressive disclosure (summary first, details linked)

## Validation Checklist

Before finalizing your skill:

- [ ] Description includes specific triggers ("Use when...")
- [ ] SKILL.md is under 100 lines
- [ ] No time-sensitive information
- [ ] Consistent terminology used throughout
- [ ] At least one concrete example included
- [ ] References are one level deep (SKILL.md links to REFERENCE.md, which links to details)
- [ ] All scripts have docstrings
- [ ] All scripts handle errors gracefully
- [ ] File and directory names follow conventions
- [ ] All links between files are relative and correct
