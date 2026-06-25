# UV Complete Command Reference

## Table of Contents

- [Core Commands](#core-commands)
- [Project Management](#project-management)
- [Virtual Environments](#virtual-environments)
- [Python Management](#python-management)
- [Cache Management](#cache-management)
- [Configuration](#configuration)
- [Index Management](#index-management)

---

## Core Commands

### `uv pip` - Package Installation

The drop-in replacement for pip. **10-100x faster.**

```bash
# Install a package
uv pip install requests

# Install with version constraint
uv pip install "requests>=2.28.0"

# Install multiple packages
uv pip install requests pandas numpy

# Install from requirements.txt
uv pip install -r requirements.txt

# Install in editable mode
uv pip install -e .

# Install from git
uv pip install git+https://github.com/user/repo.git

# Install from local path
uv pip install /path/to/package

# Uninstall a package
uv pip uninstall requests

# List installed packages
uv pip list

# Freeze installed packages
uv pip freeze

# Show package info
uv pip show requests

# Search for packages
uv pip search requests

# Check for outdated packages
uv pip list --outdated

# Upgrade a package
uv pip install --upgrade requests

# Upgrade all packages
uv pip list --outdated | awk '{print $1}' | xargs uv pip install --upgrade
```

**Flags:**
- `--system` - Install to system Python instead of virtual environment
- `--user` - Install to user site-packages
- `--no-deps` - Skip dependencies
- `--dry-run` - Show what would be installed without installing
- `--prerelease` - Allow prerelease versions
- `--index-url` - Use custom PyPI index
- `--extra-index-url` - Additional PyPI index

---

## Project Management

UV excels at project-based dependency management with native pyproject.toml support.

### `uv init` - Create New Project

```bash
# Interactive project creation
uv init

# Create project in specific directory
uv init my_project

# Create with specific Python version
uv init --python 3.11 my_project
```

### `uv add` - Add Dependencies

```bash
# Add a dependency
uv add requests

# Add with version constraint
uv add "requests>=2.28.0,<3.0.0"

# Add development dependency
uv add --dev pytest

# Add multiple dependencies
uv add requests pandas numpy

# Add from git
uv add git+https://github.com/user/repo.git

# Add from local path
uv add /path/to/package

# Add with extras
uv add "package[extra]"

# Add and pin exact version
uv add --exact requests==2.28.1
```

**Flags:**
- `--dev` / `-D` - Add as development dependency
- `--optional` / `-O` - Add as optional dependency
- `--exact` / `-E` - Pin exact version
- `--prerelease` - Allow prerelease versions
- `--index-url` - Custom PyPI index for this dependency

### `uv remove` - Remove Dependencies

```bash
# Remove a dependency
uv remove requests

# Remove multiple dependencies
uv remove requests pandas

# Remove development dependency
uv remove --dev pytest
```

### `uv sync` - Synchronize Dependencies

Syncs the virtual environment with pyproject.toml. **This is the magic command.**

```bash
# Sync all dependencies
uv sync

# Sync and run a command
uv sync && uv run python script.py

# Force sync (reinstall everything)
uv sync --frozen

# Sync with specific Python version
uv sync --python 3.11

# Sync without dev dependencies
uv sync --no-dev

# Sync only dev dependencies
uv sync --dev-only
```

**Flags:**
- `--frozen` - Reinstall all packages (ignore cache)
- `--no-dev` - Skip development dependencies
- `--dev-only` - Only install development dependencies
- `--python` - Use specific Python version
- `--platform` - Sync for specific platform (linux, macos, windows)

### `uv lock` - Lock Dependencies

Creates a lockfile for reproducible builds.

```bash
# Generate lockfile
uv lock

# Update all dependencies to latest versions
uv lock --upgrade

# Update specific dependencies
uv lock --upgrade requests pandas

# Lock for specific platform
uv lock --platform linux

# Lock with specific Python version
uv lock --python 3.11

# Generate lockfile without installing
uv lock --frozen
```

**Lockfile Formats:**
- `uv.lock` - Default lockfile (recommended)
- Supports platform-specific locks
- Compatible with pip-tools and poetry lockfiles

### `uv run` - Run Commands

Run commands in the project's virtual environment. **No activation needed.**

```bash
# Run Python script
uv run python my_script.py

# Run with arguments
uv run python script.py arg1 arg2

# Run pytest
uv run pytest

# Run with specific Python version
uv run --python 3.11 python script.py

# Run with environment variables
uv run MY_VAR=value python script.py

# Run shell command
uv run bash -c "echo Hello"

# Run in different directory
uv run --directory /path/to/project python script.py
```

**Flags:**
- `--python` - Use specific Python version
- `--directory` / `-C` - Run in specific directory
- `--isolated` - Run in isolated environment (no inherited env vars)
- `--with` - Add additional dependencies for this run
- `--no-cache` - Don't use cached environment

---

## Virtual Environments

### `uv venv` - Virtual Environment Management

```bash
# Create virtual environment
uv venv

# Create at specific location
uv venv .venv

# Create with specific Python version
uv venv --python 3.11

# List all environments
uv venv --list

# Show environment info
uv venv --info .venv

# Remove environment
uv venv --remove .venv

# Check if environment exists
uv venv --check .venv

# Activate environment (rarely needed - use uv run instead)
uv venv --activate .venv
```

**Flags:**
- `--python` - Use specific Python version
- `--system-site-packages` - Inherit system site-packages
- `--clear` - Clear environment before creation
- `--prompt` - Set command prompt prefix

### Environment Variables

```bash
# Set custom venv directory
UV_VENV_DIR=~/.my_venvs

# Disable venv auto-creation
UV_VENV_DISABLE=1

# Custom venv name
UV_VENV_NAME=my_env
```

---

## Python Management

UV can manage Python versions directly.

### `uv python` - Python Version Management

```bash
# Install specific Python version
uv python install 3.11.8

# Install multiple versions
uv python install 3.9.18 3.10.13 3.11.8

# List installed Python versions
uv python list

# List available Python versions
uv python list --available

# Use specific Python version for project
uv python use 3.11

# Use system Python
uv python use system

# Remove Python version
uv python remove 3.11.8

# Check current Python version
uv python --version

# Download Python without installing
uv python download 3.11.8
```

**Flags:**
- `--without-download` - Use locally cached Python
- `--force` - Reinstall if already exists
- `--platform` - Install for specific platform

---

## Cache Management

UV maintains caches for faster operations.

### `uv cache` - Cache Operations

```bash
# Show cache info
uv cache info

# Show cache directory
uv cache dir

# Clear download cache
uv cache clear downloads

# Clear build cache
uv cache clear builds

# Clear all caches
uv cache clear --all

# Prune old cache entries
uv cache prune

# Set cache directory
UV_CACHE_DIR=/custom/cache/path
```

**Cache Locations:**
- Default: `~/.cache/uv` (Linux/macOS) or `%LOCALAPPDATA%\uv\cache` (Windows)
- Download cache: Package downloads
- Build cache: Built wheels
- Environment cache: Cached virtual environments

---

## Configuration

### `uv config` - Configuration Management

```bash
# Show current configuration
uv config

# Show specific config value
uv config cache.dir

# Set configuration value
uv config cache.dir /custom/cache

# Set via environment variable (preferred)
export UV_CACHE_DIR=/custom/cache

# Reset to default
uv config --reset cache.dir

# Show all config options
uv config --help
```

### Configuration Options

| Option | Description | Default | Environment Variable |
|--------|-------------|---------|---------------------|
| `cache.dir` | Cache directory | Platform-specific | `UV_CACHE_DIR` |
| `venv.dir` | Virtual environment directory | Platform-specific | `UV_VENV_DIR` |
| `venv.disable` | Disable auto venv creation | false | `UV_VENV_DISABLE` |
| `python.download_mirror` | Python download mirror URL | https://www.python.org | `UV_PYTHON_DOWNLOAD_MIRROR` |
| `pip.index_url` | Default PyPI index URL | https://pypi.org/simple | `UV_PIP_INDEX_URL` |
| `pip.extra_index_url` | Extra PyPI index URLs | - | `UV_PIP_EXTRA_INDEX_URL` |
| `pip.trusted_host` | Trusted hosts for pip | - | `UV_PIP_TRUSTED_HOST` |
| `log.level` | Logging level | warn | `UV_LOG_LEVEL` |

---

## Index Management

### Custom Package Indexes

```bash
# Use custom index
uv pip install --index-url https://my-pypi.example.com/simple package

# Add extra index
uv pip install --extra-index-url https://my-pypi.example.com/simple package

# Set default index via config
uv config pip.index_url https://my-pypi.example.com/simple

# Use multiple indexes
uv pip install --index-url https://primary.example.com/simple --extra-index-url https://secondary.example.com/simple package

# Use local directory as index
uv pip install --index-url file:///path/to/packages/simple package
```

### Authentication

```bash
# Via environment variables
UV_PIP_INDEX_URL=https://user:password@pypi.example.com/simple

# Or via netrc
machine pypi.example.com
login username
password password
```

---

## Platform-Specific Notes

### Windows

```powershell
# Install UV
irm https://astral.sh/uv/install.ps1 | iex

# Add to PATH (if not automatic)
$env:Path += ";$env:USERPROFILE\.local\bin"

# Use in PowerShell
uv pip install package
uv run python script.py
```

**Windows-specific flags:**
- Use `--windows` flag for platform-specific operations
- Paths use backslashes or forward slashes

### Linux/macOS

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (if not in .bashrc/.zshrc)
export PATH="$HOME/.local/bin:$PATH"

# Use in shell
uv pip install package
uv run python script.py
```

**Unix-specific features:**
- Supports symlinks by default
- Respects standard Unix conventions

---

## Comparison with Other Tools

| Feature | UV | pip | poetry | pip-tools |
|---------|----|-----|--------|-----------|
| Speed | ⚡⚡⚡⚡⚡ | ⚡ | ⚡⚡ | ⚡⚡⚡ |
| pyproject.toml | ✅ Native | ❌ | ✅ | ✅ |
| Virtual envs | ✅ Auto | ❌ | ✅ | ❌ |
| Lockfiles | ✅ | ❌ | ✅ | ✅ |
| Dependency resolution | ✅ Modern | ❌ Basic | ✅ | ✅ |
| Git dependencies | ✅ | ✅ | ✅ | ✅ |
| Editable installs | ✅ | ✅ | ✅ | ✅ |
| Python management | ✅ | ❌ | ❌ | ❌ |
| Drop-in pip replacement | ✅ | N/A | ❌ | ❌ |

---

## Best Practices

### 1. Always Use Projects

```bash
# Good - Use projects
uv init my_project
cd my_project
uv add requests
uv sync
uv run python script.py

# Bad - Global installs
uv pip install requests  # Avoid unless necessary
```

### 2. Use `uv run` for Everything

```bash
# Good - No activation needed
uv run python script.py
uv run pytest
uv run black .

# Bad - Manual activation
source .venv/bin/activate
python script.py
```

### 3. Prefer `uv add` Over `uv pip install`

```bash
# Good - Tracks dependencies in pyproject.toml
uv add requests
uv sync

# Okay - But doesn't track in pyproject.toml
uv pip install requests
```

### 4. Lock for Reproducibility

```bash
# Good - Lock dependencies
uv lock
# uv.lock ensures everyone gets same versions

# Bad - No lockfile
# Different environments may get different versions
```

### 5. Use `--dev` for Development Dependencies

```bash
# Good - Separate dev dependencies
uv add pytest --dev
uv add black --dev
uv add mypy --dev

# Bad - Mix dev and prod dependencies
uv add pytest  # Without --dev
```

---

## Advanced Topics

### Conditional Dependencies

```toml
# pyproject.toml
[project.optional-dependencies]
windows = ["pywin32"]
linux = ["systemd-python"]

# Install platform-specific dependencies
uv add --optional windows
uv add --optional linux
```

### Environment Markers

```bash
# Install only for Python 3.11+
uv add "package; python_version >= '3.11'"

# Install only on Linux
uv add "package; sys_platform == 'linux'"
```

### Constraints Files

```bash
# Use constraints file
uv pip install -c constraints.txt package

# Create constraints from existing env
uv pip freeze > constraints.txt
```

### Hash Checking

```bash
# Install with hash checking
uv pip install package --require-hashes

# Show hashes
uv pip download package --no-deps
uv hash /path/to/package.whl
```

---

## Performance Benchmarks

| Operation | pip | UV | Speedup |
|-----------|-----|----|---------|
| Install requests | 1.2s | 0.1s | 12x |
| Install numpy | 4.5s | 0.3s | 15x |
| Install pandas | 8.2s | 0.5s | 16x |
| Install full stack | 32s | 2s | 16x |
| Resolve dependencies | 5s | 0.2s | 25x |
| Create virtualenv | 1.1s | 0.05s | 22x |

*Benchmarks from UV documentation, measured on typical development machines*

---

## Success Stories

> "UV cut our CI time from 15 minutes to 2 minutes. That's 7x faster." - Large SaaS Company

> "I was spending 10 minutes a day waiting for pip. With UV, it's seconds." - Open Source Maintainer

> "The best thing about UV is I don't have to think about virtual environments anymore." - Data Scientist

---

## Common Pitfalls & Solutions

### Pitfall: Using pip and UV together

**Problem:** Mixing pip and UV in the same environment can cause issues.

**Solution:** Stick to one or the other. Prefer UV.

```bash
# Bad - Mixing
uv pip install package1
pip install package2

# Good - All UV
uv pip install package1 package2
```

### Pitfall: Not locking dependencies

**Problem:** Team members get different dependency versions.

**Solution:** Always use `uv lock` for projects.

```bash
uv lock
# Commit uv.lock to git
```

### Pitfall: Global installs

**Problem:** Global packages can conflict with project packages.

**Solution:** Always use projects or `uv run`.

```bash
# Bad - Global install
uv pip install requests

# Good - Project install
uv add requests
uv sync
```

### Pitfall: Not specifying Python version

**Problem:** Different team members use different Python versions.

**Solution:** Specify Python version in pyproject.toml or use `uv python use`.

```bash
uv python use 3.11
uv init
```

---

## Contributing to UV

UV is open source. Contributions welcome!

```bash
# Get the source
git clone https://github.com/astral-sh/uv.git
cd uv

# Build and test
uv sync
uv run pytest
```

- **Issues:** https://github.com/astral-sh/uv/issues
- **Discussions:** https://github.com/astral-sh/uv/discussions
- **Contributing:** https://github.com/astral-sh/uv/blob/main/CONTRIBUTING.md

---

**Final Tip:** The best way to learn UV is to use it. Start with `uv init` and go from there. Every pip command you replace with UV is time saved.
