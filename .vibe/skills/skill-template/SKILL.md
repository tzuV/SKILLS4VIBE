---
name: skill-template
description: A template demonstrating proper skill structure and best practices. Use when creating new skills or needing a reference for skill formatting.
---

# Skill Template

This is a template demonstrating the ideal structure for a Vibe skill. Use this as a starting point when creating new skills.

## Quick Start

1. Copy this entire `skill-template/` directory
2. Rename it to your skill name (lowercase, hyphen-separated)
3. Update `SKILL.md` with your content
4. Add `REFERENCE.md` and `EXAMPLES.md` if content exceeds 100 lines
5. Add scripts in `scripts/` if deterministic operations are needed

## Core Principles

- **Single purpose**: Each skill solves one specific problem
- **Progressive disclosure**: Start with essentials, link to details
- **Self-contained**: All required resources bundled in the directory
- **Discoverable**: Description clearly states triggers and use cases

## When to Use This Template

- Creating a new agent capability
- Refactoring an existing monolithic skill
- Documenting a complex workflow
- Bundling reusable code with instructions

## File Structure

```
skill-name/
├── SKILL.md           # Required: Main instructions
├── REFERENCE.md       # Optional: Detailed documentation
├── EXAMPLES.md        # Optional: Usage examples
└── scripts/           # Optional: Utility scripts
    ├── validate.py
    └── helper.js
```

See [REFERENCE.md](REFERENCE.md) for detailed file specifications.
See [EXAMPLES.md](EXAMPLES.md) for complete working examples.
