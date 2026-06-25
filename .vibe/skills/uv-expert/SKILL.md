---
name: uv-expert
description: Expert guidance on UV, the ultra-fast Python package manager. Use when user mentions UV, pip, Python packaging, dependency management, virtual environments, or asks about faster pip alternatives.
---

# UV Expert - The Ultra-Fast Python Package Manager

## Why UV?

UV is **10-100x faster** than pip. It's written in Rust, designed for performance, and replaces pip, virtualenv, pip-tools, and poetry in a single command. Stop waiting for pip installs.

**Key benefits:**
- ⚡ **Blazing fast** - Install packages in milliseconds, not seconds
- 🎯 **Single command** - `uv pip` replaces pip, virtualenv, pip-tools
- 📦 **Modern workflow** - Built for Python 3.8+, with native pyproject.toml support
- 🔧 **Drop-in replacement** - Compatible with existing pip workflows
- 🏗️ **Project isolation** - Automatic virtualenv management

## Quick Start

### Install UV

```bash
# Official installer (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip (ironic, but works)
pip install uv

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### First Steps

```bash
# Create a new project
uv init my_project
cd my_project

# Add dependencies
uv add requests pandas

# Install everything
uv sync

# Run your script
uv run python my_script.py
```

## Workflows

### Everyday Commands

| What you'd do with pip | Do this with UV | Speedup |
|------------------------|-----------------|---------|
| `pip install package` | `uv pip install package` | 10-100x |
| `pip install -r requirements.txt` | `uv pip install -r requirements.txt` | 10-100x |
| `python -m venv .venv` + `source .venv/bin/activate` | `uv venv` (auto-managed) | Instant |
| `pip freeze > requirements.txt` | `uv pip freeze > requirements.txt` | 10-100x |
| `pip uninstall package` | `uv pip uninstall package` | 10-100x |

### Project Management

```bash
# Create new project with pyproject.toml
uv init

# Add dependency to project
uv add requests

# Add dev dependency
uv add --dev pytest black

# Sync environment with pyproject.toml
uv sync

# Run command in project environment
uv run pytest
uv run black .
```

### Virtual Environments

```bash
# Create virtual environment
uv venv

# Create at specific location
uv venv .venv

# List environments
uv venv --list

# Remove environment
uv venv --remove .venv
```

### Dependency Management

```bash
# Install from pyproject.toml
uv sync

# Install from requirements.txt
uv pip install -r requirements.txt

# Export locked dependencies
uv lock

# Update all dependencies
uv lock --upgrade

# Add dependency with version constraint
uv add "requests>=2.28.0"

# Add from git
uv add "git+https://github.com/user/repo.git"
```

### Running Scripts

```bash
# Run Python script in project environment
uv run python my_script.py

# Run any command in project environment
uv run pytest tests/
uv run black .
uv run mypy .

# Run with specific Python version
uv run --python 3.11 python script.py
```

## Migration Guide

### From pip + virtualenv

```bash
# Before (slow)
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python script.py

# After (fast)
uv pip install -r requirements.txt
uv run python script.py
```

### From pip-tools

```bash
# Before
pip-compile
pip-sync

# After
uv lock
uv sync
```

### From Poetry

```bash
# Before
poetry add requests
poetry install
poetry run pytest

# After
uv add requests
uv sync
uv run pytest
```

## Performance Tips

- **Use `uv pip` instead of `pip`** - Even without projects, it's faster
- **`uv sync` for project dependencies** - Resolves and installs in one step
- **`uv run` for one-off commands** - No need to activate virtualenv
- **Cache is automatic** - UV caches downloads and builds

## When to Use What

| Command | Use when... |
|---------|-------------|
| `uv pip install` | Installing packages globally or in active venv |
| `uv add` | Adding dependencies to a project |
| `uv sync` | Syncing project dependencies from pyproject.toml |
| `uv run` | Running commands in project environment |
| `uv venv` | Managing virtual environments |
| `uv lock` | Locking dependencies for reproducible builds |

## Common Patterns

### Creating a New Project

```bash
uv init my_awesome_project
cd my_awesome_project
uv add fastapi uvicorn
# Edit pyproject.toml to add your own code
uv run uvicorn main:app --reload
```

### Adding a Dependency

```bash
# Simple
uv add requests

# With version
uv add "numpy>=1.24.0"

# Development dependency
uv add --dev pytest hypothesis

# From GitHub
uv add "git+https://github.com/psf/requests.git"
```

### Running Tests

```bash
# One-time run
uv run pytest

# With coverage
uv run pytest --cov=my_package

# Specific test
uv run pytest tests/test_feature.py
```

### Managing Python Versions

```bash
# Use specific Python version for project
uv python use 3.11

# Install specific Python version
uv python install 3.11.8

# List installed Python versions
uv python list
```

## Remember This

✅ **UV is faster** - Use it instead of pip whenever possible
✅ **`uv run` is magic** - No more `source .venv/bin/activate`
✅ **Projects > Global** - Prefer `uv add` + `uv sync` over global installs
✅ **Compatible** - Works with existing pip workflows

## Troubleshooting

### "Command not found"

Make sure UV is on your PATH. The installer should handle this, but if not:
- Linux/macOS: Add `~/.local/bin` to your PATH
- Windows: Add `%USERPROFILE%\.local\bin` to your PATH

### Slow installs

UV should be fast by default. If it's slow:
- Check your internet connection
- Try `uv cache clear` to clear the cache
- Make sure you're using the latest version: `uv --version`

### Dependency conflicts

UV uses a modern resolver. If you get conflicts:
- Run `uv lock --upgrade` to update all dependencies
- Check your version constraints in pyproject.toml
- Use `uv add` to let UV pick compatible versions

## Version Check

```bash
# Check UV version
uv --version

# Update UV
uv self update
```

## Resources

- **Official site**: https://uv.pypa.io
- **GitHub**: https://github.com/astral-sh/uv
- **Docs**: https://docs.astral.sh/uv
- **Comparison**: UV vs pip vs poetry vs pip-tools

---

**Remember: Every time you use pip, UV is waiting to save you time. Make the switch today.**
