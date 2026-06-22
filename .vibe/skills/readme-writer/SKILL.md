---
name: readme-writer
description: Generate and maintain project README files, markdown content, and codebase documentation. Use when user requests README generation, markdown formatting, codebase summarization, or step-by-step tutorials.
---

# README Writer

## Quick Start

**Trigger phrases:**
- "write a README"
- "update README"
- "generate documentation"
- "format this as markdown"
- "summarize this codebase"
- "create a tutorial"

**Basic usage:**
1. User requests documentation
2. I explore the codebase structure
3. I generate appropriate README content
4. I format with proper markdown

## Workflows

### Generate Project README
1. Read project structure and metadata (package.json, pyproject.toml, setup.py, etc.)
2. Identify key files, directories, and dependencies
3. Extract package info (name, version, description, author, license)
4. Detect language/framework from file extensions and config files
5. Generate standard README sections:
   - Title with badges (language, CI, license, version)
   - Clear description
   - Table of Contents (for larger projects)
   - Installation instructions
   - Usage examples
   - API Reference (for libraries)
   - Configuration (if applicable)
   - Contributing guidelines
   - License

### Markdown Formatting
- Convert data to markdown tables
- Format code blocks with proper syntax highlighting
- Create proper heading hierarchy (H1 for title only, H2 for sections, H3+ for subsections)
- Generate lists and checklists
- Format links and images
- Create definition lists where appropriate

### Codebase Summarization
- Generate file tree overview with annotations
- Identify module dependencies
- Highlight key functionality
- Note test coverage
- Identify entry points and main files

### Step-by-Step Tutorials
- Setup instructions (prerequisites, installation)
- Running the code (commands, flags, options)
- Example use cases with code snippets
- Expected output descriptions
- Troubleshooting common issues

## Output Standards

### README Structure
Always include in this order:
1. Title (H1)
2. Badges (if applicable)
3. Description
4. Table of Contents (if README > 100 lines)
5. Installation
6. Usage
7. (Optional sections based on project type)
8. License

### Formatting Rules
- Use consistent heading levels
- Always use code fences with language tags
- Use relative paths for internal links
- Keep lines under 100 characters where possible
- Use consistent indentation (2 or 4 spaces, matching project)
- Prefer bullet lists over numbered unless order matters

### Language Detection
Detect project language from:
- File extensions (.py, .js, .ts, .go, .rs, etc.)
- Configuration files (package.json, pyproject.toml, go.mod, etc.)
- Framework indicators (next.config.js, vite.config.ts, etc.)

Use detected language for:
- Badge selection
- Installation commands
- Code block language tags
- Example formatting

## Quality Guidelines

### README Quality Checklist
- [ ] Title matches project name
- [ ] Description is clear and concise
- [ ] Installation instructions are tested
- [ ] At least one usage example is provided
- [ ] All code blocks have language tags
- [ ] Links are valid (if possible to verify)
- [ ] License is specified

### When to Include Sections
- **Badges:** Only if CI/CD, coverage, version, or license info is available
- **Screenshots:** Only for UI/visual projects
- **API Reference:** Only for library/package projects
- **Contributing:** Only for open-source projects expecting contributions
- **Changelog:** Only if maintaining version history
- **Roadmap:** Only for active development projects

### Tone
- Professional but approachable
- Direct and clear
- Avoid excessive marketing language
- Use imperative mood for instructions
- Keep examples minimal but complete
