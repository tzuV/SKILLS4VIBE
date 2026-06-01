# SKILLS4VIBE

A reusable collection of skills for Mistral's Vibe CLI. Share, discover, and collaborate on agent capabilities with other developers.

## Quick Start

### For Consumers (Using Shared Skills)

1. **Trust the project folder** in your Vibe configuration:
   ```
   Add to ~/.vibe/trusted_folders.toml:
   [folders]
   "SKILLS4VIBE" = "~/SKILLS4VIBE"
   ```

2. **Clone or pull the repository:**
   ```bash
   git clone https://github.com/tzuV/SKILLS4VIBE.git
   # or update existing:
   git pull origin main
   ```

3. **Vibe automatically discovers skills** from the `.vibe\skills\` directory when the folder is trusted or use /reload.

4. **Use skills** 

### For Contributors (Sharing Your Skills)

1. **Create your skill** following the structure below
2. **Test it locally** by triggering it in Vibe sessions
3. **Commit and push** to share with collaborators:
   ```bash
   git add .vibe\skills\your-skill\*
   git commit -m "Add your-skill: brief description"
   git push origin main
   ```
4. **Collaborators pull updates** to access your new skill

---

## Skill Structure

Each skill is a self-contained capability that Vibe can load when relevant to the user's request.

```
.vibe\skills\skill-name\
├── SKILL.md           # Required: Main instructions
├── REFERENCE.md       # Optional: Detailed documentation
├── EXAMPLES.md        # Optional: Usage examples
└── scripts\           # Optional: Utility scripts
    └── helper.py
```

### SKILL.md Format

Every skill **must** start with YAML frontmatter:

```markdown
---
name: skill-name
description: Brief capability description. Use when [specific triggers].
---

# Skill Title

## Instructions
[Your detailed workflow, rules, and guidelines]
```

**Critical: The description field is the only thing Vibe sees when deciding which skill to load.** Make it specific and include trigger phrases.



## Creating a New Skill

Use the `write-a-skill` skill to guide you through creating a well-structured skill:

```
> use the write-a-skill skill
```


## Current Skills

| Skill | Description | Best For |
|-------|-------------|----------|
| [caveman](.vibe/skills/caveman/SKILL.md) | Ultra-compressed communication (75% fewer tokens) | Reducing token usage, technical discussions |
| [diagnosis](.vibe/skills/diagnosis/SKILL.md) | Structured debugging workflow | Bug hunting, performance issues |
| [grill-me](.vibe/skills/grill-me/SKILL.md) | Rigorous design review | Architecture decisions, plan validation |
| [improve-codebase](.vibe/skills/improve-codebase/SKILL.md) | Architectural improvements | Refactoring, codebase navigation |
| [plan](.vibe/skills/plan/SKILL.md) | Technical planning | Project blueprints, stack decisions |
| [prototype](.vibe/skills/prototype/SKILL.md) | Rapid prototyping | Design exploration, UI mockups |
| [reusability](.vibe/skills/reusability/SKILL.md) | Code consolidation | Utility extraction, DRY principles |
| [tdd](.vibe/skills/tdd/SKILL.md) | Test-driven development | Feature building, bug fixing |
| [to-prd](.vibe/skills/to-prd/SKILL.md) | PRD creation | Documentation, issue tracking |
| [write-a-skill](.vibe/skills/write-a-skill/SKILL.md) | Skill creation guide | Building new skills |
| [zoom-out](.vibe/skills/zoom-out/SKILL.md) | Context expansion | Codebase understanding |

---

## File Structure

```
SKILLS4VIBE/
├── .vibe/
│   └── skills/
│       ├── caveman/
│       │   └── SKILL.md
│       ├── diagnosis/
│       │   └── SKILL.md
│       ├── [your-skill]/
│       │   ├── SKILL.md
│       │   ├── REFERENCE.md (optional)
│       │   ├── EXAMPLES.md (optional)
│       │   └── scripts/ (optional)
│       │       └── helper.py
│       └── ...
├── README.md
└── .git/
```

## Contributing

1. Fork the repository
2. Create a new skill or improve an existing one
3. Test thoroughly
4. Submit a pull request with:
   - Clear description of what the skill does
   - When it should be triggered
   - Any dependencies or prerequisites

### Review Criteria

Pull requests will be evaluated on:
- [ ] Proper skill structure and frontmatter
- [ ] Clear, specific description with triggers
- [ ] Useful, non-duplicative capability
- [ ] Well-documented workflow
- [ ] Follows best practices above

---

## License

This project is open source. Feel free to use, modify, and share these skills according to the repository's license terms.

## Resources

- [Vibe CLI Documentation](https://github.com/mistralai/vibe-cli)
- [Skill Writing Guide](.vibe/skills/write-a-skill/SKILL.md)
- [Issue Tracker](https://github.com/tzuV/SKILLS4VIBE/issues)
