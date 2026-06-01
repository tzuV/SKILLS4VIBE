# SKILLS4VIBE

A reusable collection of skills for Mistral's Vibe CLI. Share, discover, and collaborate on agent capabilities with other developers.

## Quick Start

### For Consumers (Using Shared Skills)

1. **Trust the project folder** in your Vibe configuration:
   ```
   Add to ~/.vibe/trusted_folders.toml:
   [folders]
   "SKILLS4VIBE" = "C:/Users/jakob/PycharmProjects/SKILLS4VIBE"
   ```

2. **Clone or pull the repository:**
   ```bash
   git clone https://github.com/tzuV/SKILLS4VIBE.git
   # or update existing:
   git pull origin main
   ```

3. **Vibe automatically discovers skills** from the `.vibe\skills\` directory when the folder is trusted.

4. **Use skills** by referencing them in conversations:
   - "use the diagnosis skill"
   - "load the tdd skill"
   - "I need to prototype this"

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

#### Good Description Example:
```yaml
description: Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
```

#### Bad Description Example:
```yaml
description: Helps with testing.
```
*Why it's bad: Too vague, no trigger phrases, agent can't distinguish from other testing-related skills.*

---

## Creating a New Skill

Use the `write-a-skill` skill to guide you through creating a well-structured skill:

```
> use the write-a-skill skill
```

Or follow these steps manually:

1. **Choose a name** - Short, descriptive, kebab-case (e.g., `pdf-extractor`, `api-design`)
2. **Create the directory:** `.vibe\skills\your-skill-name\`
3. **Create SKILL.md** with proper frontmatter and clear instructions
4. **Add supporting files** if needed:
   - `REFERENCE.md` - For detailed documentation (>100 lines)
   - `EXAMPLES.md` - For usage examples and templates
   - `scripts\` - For reusable utility code

5. **Follow the checklist:**
   - [ ] Description includes trigger phrases ("Use when...")
   - [ ] SKILL.md is under 100 lines (split if longer)
   - [ ] No time-sensitive information
   - [ ] Consistent terminology with project domain
   - [ ] Concrete examples included
   - [ ] References are one level deep

---

## Skill Discovery

Vibe agents discover and select skills based on:

1. **The description field** in the frontmatter (primary)
2. **The skill name** (secondary)
3. **Content of SKILL.md** (tertiary)

**Optimize for discovery:**
- Include **specific trigger phrases** users might say
- Mention **domain keywords** (e.g., "PDF", "database", "React")
- State **when to use** the skill
- Keep it **concise but specific** (max ~200 characters recommended)

---

## Collaboration Workflow

### For Teams

1. **Central repository** (this repo) holds the canonical skill set
2. **Branch per feature** for new skills or major updates:
   ```bash
   git checkout -b skill/new-feature
   ```
3. **Pull requests** for review before merging to main
4. **Version tags** for stable releases (optional):
   ```bash
   git tag -a v1.0.0 -m "Stable skill set v1"
   git push origin v1.0.0
   ```

### For Individuals Sharing Skills

1. **Fork this repository**
2. **Add your skills** to your fork
3. **Share with specific collaborators** by:
   - Adding them as collaborators to your fork
   - Sharing the repository URL
   - Exporting individual skill files

### Syncing with Upstream

To get updates from the main repository:

```bash
# Add upstream remote (if not already added)
git remote add upstream https://github.com/tzuV/SKILLS4VIBE.git

# Fetch and merge updates
git fetch upstream
git merge upstream/main

# Resolve any conflicts, then push to your fork
git push origin main
```

---

## Best Practices

### Skill Organization

- **One capability per skill** - Don't bundle unrelated capabilities
- **Atomic and focused** - Skills should do one thing well
- **Composable** - Skills can reference each other when appropriate
- **Avoid duplication** - Check existing skills before creating new ones

### Descriptions

Follow the formula:
```
[What it does]. Use when [trigger phrase 1], [trigger phrase 2], or [context].
```

### Documentation

- **SKILL.md**: Core workflow and rules
- **REFERENCE.md**: Detailed explanations, theory, background
- **EXAMPLES.md**: Concrete examples, templates, snippets
- **scripts/**: Reusable code, validation scripts, helpers

### Testing Your Skill

Before committing:
1. Trigger the skill in a Vibe session with various phrasings
2. Verify it activates when expected
3. Verify it doesn't activate for unrelated requests
4. Test edge cases mentioned in the skill

---

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

---

## Troubleshooting

### Skills not being discovered?
- Verify the folder is in `.vibe\trusted_folders.toml`
- Check the skill has proper YAML frontmatter with `name` and `description`
- Ensure the skill directory is under `.vibe\skills\`
- Restart your Vibe session

### Skill not triggering when expected?
- Review the description - does it include the trigger phrase you used?
- Check for typos in the skill name or description
- Try rephrasing your request to match the description better

### Want to disable a skill temporarily?
- Move it out of the `.vibe\skills\` directory
- Or rename the directory (add a prefix like `_disabled-`)

---

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
