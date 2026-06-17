---
name: vibe
description: Understand the Vibe CLI application internals: configuration, VIBE_HOME structure, available parameters, agents, skills, tools, and how to inspect or update the user's setup. Use this skill when the user asks about how Vibe works, wants to configure it, or when you need to understand the runtime environment.
---

# Vibe CLI Internals

## Overview

Mistral Vibe CLI is a powerful command-line interface for interacting with AI models. This skill provides insights into its configuration, structure, and available features.

## Configuration

### VIBE_HOME
The primary configuration directory is located at `%USERPROFILE%\.vibe` on Windows or `~/.vibe` on Unix systems. This directory contains:
- `logs/`: Conversation history and logs
- `skills/`: Custom and built-in skills
- Agent configurations

### Main Configuration File
Located at `%VIBE_HOME%\config.yaml` or `%VIBE_HOME%\config.json`, this file contains:
- Model settings
- API endpoints
- Default parameters
- Agent definitions

## Available Parameters

### Model Parameters
- `--model`: Specify the model to use (e.g., mistral-medium, mistral-large)
- `--temperature`: Control randomness (0.0-2.0)
- `--max-tokens`: Limit response length
- `--top-p`: Nucleus sampling parameter

### Session Parameters
- `--session`: Load a specific conversation session
- `--new-session`: Start a fresh conversation
- `--list-sessions`: List all available sessions

### Agent Parameters
- `--agent`: Specify the agent profile to use
- `--list-agents`: List all available agents
- `--create-agent`: Create a new agent profile

## Agents

Agents define different AI personalities and capabilities. The system prompt and AGENTS.md files define:
- Agent behavior constraints
- Available tools
- Communication style
- Specialized workflows

## Skills

Skills are modular capabilities that can be loaded on demand. Each skill has:
- A `SKILL.md` file with instructions
- Optional bundled resources (scripts, templates)
- Specific triggers or invocation methods

### Skill Structure
```
skill-name/
├── SKILL.md          # Skill instructions and workflows
├── scripts/          # Helper scripts
│   └── *.py
├── templates/        # Template files
│   └── *.md
└── requirements.txt  # Dependencies
```

### Invoking Skills
Use the `/` prefix to invoke skills:
- `/caveman` - Ultra-compressed communication
- `/diagnosis` - Structured debugging
- `/plan` - Project planning
- etc.

## Tools

Available tools include:
- File operations (read, write, edit)
- Code execution (bash, python)
- Search (grep, web_search)
- Git operations
- Task management
- Agent delegation

## Inspecting the Setup

### Check Current Configuration
```bash
# View Vibe CLI version
vibe --version

# View current configuration
vibe --config

# List available skills
vibe --list-skills

# List available agents
vibe --list-agents
```

### Environment Variables
- `VIBE_HOME`: Override the default configuration directory
- `VIBE_MODEL`: Default model to use
- `VIBE_API_KEY`: API key for authentication

## Updating the Setup

### Adding New Skills
1. Create a new directory under `.vibe/skills/`
2. Add a `SKILL.md` file with skill instructions
3. Include any necessary scripts or templates
4. Register the skill in the configuration

### Modifying Configuration
Edit the configuration files in your VIBE_HOME directory to customize:
- Model preferences
- Agent behaviors
- Tool availability
- Default settings

## Runtime Environment

### File Structure
```
%VIBE_HOME%/
├── config.yaml          # Main configuration
├── logs/               # Conversation logs
│   └── sessions/       # Individual sessions
├── skills/             # Available skills
│   └── skill-name/     # Each skill directory
│       ├── SKILL.md
│       └── resources/
├── agents/             # Agent definitions
└── temp/               # Temporary files
```

### Session Management
- Sessions are stored as markdown files
- Each session has a unique timestamp-based ID
- Session metadata includes model, timestamp, and parameters

## Useful Commands

```bash
# Start a new session
vibe new

# Continue previous session
vibe

# List all sessions
vibe --list

# Search sessions
vibe --search "query"

# Clear all sessions
vibe --clear

# View configuration
vibe --config

# Update Vibe
vibe --update
```

## Workflows

### Understanding Your Setup
1. Check VIBE_HOME location
2. Review configuration files
3. List available skills and agents
4. Verify tool availability

### Debugging Issues
1. Check logs for errors
2. Verify API connectivity
3. Test with different models
4. Review agent constraints

### Customizing Vibe
1. Create custom agents with AGENTS.md
2. Add new skills with SKILL.md
3. Configure default parameters
4. Set up environment variables
