# UV Usage Examples - Real-World Scenarios

## Table of Contents

- [Web Development](#web-development)
- [Data Science](#data-science)
- [CLI Applications](#cli-applications)
- [Libraries](#libraries)
- [Testing](#testing)
- [Deployment](#deployment)
- [CI/CD](#cicd)
- [Everyday Tasks](#everyday-tasks)

---

## Web Development

### FastAPI Application

```bash
# Create new FastAPI project
uv init fastapi-app
cd fastapi-app

# Add core dependencies
uv add fastapi uvicorn

# Add dev dependencies
uv add --dev pytest httpx pyright ruff

# Create main.py
cat > main.py << 'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
EOF

# Run development server
uv run uvicorn main:app --reload

# Run tests
uv run pytest

# Type checking
uv run pyright

# Linting
uv run ruff check .

# Lock dependencies for production
uv lock

# Sync for production (no dev dependencies)
uv sync --no-dev --frozen
```

**Project Structure:**
```
fastapi-app/
├── main.py
├── pyproject.toml
├── uv.lock
└── .venv/ (auto-managed)
```

**Time saved:** 
- FastAPI + uvicorn install: pip ~8s → UV ~0.8s (10x faster)
- Development server startup: ~2s faster with UV

---

### Django Project

```bash
# Create Django project
uv init django-app
cd django-app

# Add Django
uv add django psycopg2-binary

# Add dev dependencies
uv add --dev pytest pytest-django black isort

# Create Django project
uv run django-admin startproject myproject .

# Migrate and run
uv run python manage.py migrate
uv run python manage.py runserver

# Run tests
uv run pytest

# Format code
uv run black . && uv run isort .
```

**Django Settings for UV:**
```python
# settings.py
import os

# UV automatically creates .venv, reference it
BASE_DIR = Path(__file__).resolve().parent.parent

# No need for pip-specific settings
INSTALLED_APPS = [...]
```

---

### Flask Application

```bash
# Quick Flask app
uv init flask-app
cd flask-app

uv add flask gunicorn
uv add --dev pytest flask-testing

# Create app.py
cat > app.py << 'EOF'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, UV!"
EOF

# Run development server
uv run flask run

# Run production server
uv run gunicorn -w 4 app:app

# Test
uv run pytest
```

---

## Data Science

### Jupyter Notebook Environment

```bash
# Create data science project
uv init data-analysis
cd data-analysis

# Add data science stack
uv add numpy pandas matplotlib scikit-learn jupyter

# Add dev dependencies
uv add --dev pytest mypy

# Launch Jupyter
uv run jupyter notebook

# Run Python script
uv run python analyze.py

# Install specific versions for reproducibility
uv add "numpy==1.24.3" "pandas==2.0.3"
uv lock
```

**Kernel Setup:**
```bash
# Create kernel for Jupyter
uv run python -m ipykernel install --user --name=data-analysis
```

**Time saved:**
- numpy install: pip ~25s → UV ~2s (12x faster)
- pandas install: pip ~45s → UV ~3s (15x faster)

---

### Machine Learning Project

```bash
# ML project with GPU support
uv init ml-project
cd ml-project

# Core ML packages
uv add torch torchvision torchaudio
# Or for TensorFlow:
# uv add tensorflow

# Training dependencies
uv add datasets transformers accelerate

# Dev dependencies
uv add --dev pytest tensorboard

# Create train.py
cat > train.py << 'EOF'
import torch
from datasets import load_dataset

# Training code...
EOF

# Run training
uv run python train.py

# Start tensorboard
uv run tensorboard --logdir runs/
```

**GPU Note:** UV handles CUDA versions automatically when possible.

---

### Data Pipeline

```bash
# ETL pipeline
uv init data-pipeline
cd data-pipeline

# Add pipeline dependencies
uv add pandas pyarrow polars bonobo dask

# Add dev dependencies
uv add --dev pytest hypothesis

# Create pipeline.py
cat > pipeline.py << 'EOF'
import pandas as pd
import polars as pl

# ETL logic...
EOF

# Run pipeline
uv run python pipeline.py

# Process with Dask
uv add dask[complete]
uv run python -c "import dask; print(dask.__version__)"
```

---

## CLI Applications

### Simple CLI Tool

```bash
# Create CLI tool
uv init my-cli
cd my-cli

# Add Click for CLI
uv add click

# Add dev dependencies
uv add --dev pytest pytest-click

# Create cli.py
cat > cli.py << 'EOF'
import click

@click.command()
@click.argument('name')
def hello(name):
    click.echo(f"Hello, {name}! From UV!")

if __name__ == '__main__':
    hello()
EOF

# Make executable
uv run python -m pip install --editable .
# Or just run directly
uv run python cli.py World

# Install as CLI command
uv add --editable .
uv sync
my-cli World  # Now available globally in venv
```

---

### Rich CLI Application

```bash
# Fancy CLI with Rich
uv init fancy-cli
cd fancy-cli

uv add rich click
uv add --dev pytest

# Create app.py
cat > app.py << 'EOF'
from rich.console import Console
import click

console = Console()

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.argument('name')
def hello(count, name):
    for i in range(count):
        console.print(f"[bold green]Hello[/bold green] [blue]{name}[/blue]! ({i+1}/{count})")

if __name__ == '__main__':
    hello()
EOF

# Run
uv run python app.py --count=5 World
```

---

## Libraries

### Publishing a Library

```bash
# Create library project
uv init my-library
cd my-library

# Add library dependencies
uv add requests pydantic

# Add dev dependencies
uv add --dev pytest pytest-cov mypy ruff build twine

# Create library structure
mkdir -p my_library
cat > my_library/__init__.py << 'EOF'
"""My amazing library powered by UV."""
__version__ = "0.1.0"
EOF

# Write tests
test/ test_library.py

# Run tests
uv run pytest --cov=my_library

# Type check
uv run mypy my_library

# Lint
uv run ruff check .

# Build package
uv run python -m build

# Publish to PyPI
uv run twine upload dist/*
```

**pyproject.toml for Libraries:**
```toml
[project]
name = "my-library"
version = "0.1.0"
description = "My amazing library"
authors = [{ name = "Your Name", email = "you@example.com" }]
dependencies = ["requests>=2.28.0", "pydantic>=2.0.0"]

[project.optional-dependencies]
dev = ["pytest>=7.0.0", "pytest-cov>=4.0.0"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

### Type-Checked Library

```bash
# Library with full type support
uv init typed-library
cd typed-library

# Add typing support
uv add pydantic typing-extensions
uv add --dev mypy pyright pytest

# Create typed module
cat > typed_library/models.py << 'EOF'
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
EOF

# Run type checker
uv run mypy typed_library

# Or with pyright (faster)
uv run pyright typed_library
```

---

## Testing

### Testing Workflow

```bash
# Full testing setup
uv init tested-project
cd tested-project

# Add main dependency
uv add requests

# Add comprehensive test dependencies
uv add --dev pytest pytest-cov pytest-mock hypothesis pytest-xdist
uv add --dev pytest-asyncio pytest-django  # As needed

# Create tests
test/ test_basic.py

# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=my_project --cov-report=html

# Run specific test
uv run pytest test_basic.py::test_function

# Run with multiple workers
uv run pytest -n auto

# Run only markers
uv run pytest -m slow

# Watch for changes (with pytest-watch)
uv add --dev pytest-watch
uv run ptw . -- -n auto
```

---

### Integration Testing

```bash
# Integration test with test database
uv init integration-tests
cd integration-tests

uv add fastapi sqlalchemy psycopg2-binary httpx
uv add --dev pytest pytest-asyncio testcontainers

# Create integration tests
test/ test_integration.py

# Run integration tests
uv run pytest test_integration.py

# With test containers (PostgreSQL)
uv run pytest --tc-postgresql:14 test_integration.py
```

---

## Deployment

### Docker Container

```bash
# Create Docker-ready project
uv init docker-app
cd docker-app

# Add dependencies
uv add fastapi uvicorn

# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

# Install UV in container
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app
COPY . .

# Sync dependencies
RUN uv sync --no-dev --frozen

# Copy project
COPY . .

# Run
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
EOF

# Build and run
# docker build -t myapp .
# docker run -p 8000:8000 myapp

# Or use UV directly in container
# docker run -it python:3.11-slim bash -c "curl -LsSf https://astral.sh/uv/install.sh | sh && uv --version"
```

**Docker Optimization:**
```dockerfile
# Multi-stage build for smaller image
FROM python:3.11-slim as builder
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /app
COPY pyproject.toml .
RUN uv lock

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/uv.lock .
COPY . .
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
RUN uv sync --no-dev --frozen
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
```

---

### Serverless Deployment

```bash
# AWS Lambda with UV
uv init lambda-function
cd lambda-function

# Add dependencies (keep minimal for Lambda)
uv add boto3 requests

# Create handler.py
cat > handler.py << 'EOF'
def lambda_handler(event, context):
    import requests
    return {
        'statusCode': 200,
        'body': 'Hello from UV-powered Lambda!'
    }
EOF

# Package for Lambda
uv sync --no-dev --frozen --platform linux
# Zip .venv/lib/python*/site-packages and handler.py
# Upload to AWS Lambda
```

---

## CI/CD

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install UV
        run: |
          curl -LsSf https://astral.sh/uv/install.sh | sh
          echo "$HOME/.local/bin" >> $GITHUB_PATH
      
      - name: Install dependencies
        run: uv sync --no-dev
      
      - name: Run tests
        run: uv run pytest
      
      - name: Run type check
        run: uv run mypy .
      
      - name: Run lint
        run: uv run ruff check .
```

**Time saved in CI:**
- Dependency install: pip ~45s → UV ~3s (15x faster)
- Full CI run: ~2min → ~15s with UV

---

### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build

test:
  stage: test
  image: python:3.11
  before_script:
    - curl -LsSf https://astral.sh/uv/install.sh | sh
    - export PATH="$HOME/.local/bin:$PATH"
    - uv sync
  script:
    - uv run pytest
    - uv run mypy .
    - uv run ruff check .

build:
  stage: build
  image: python:3.11
  before_script:
    - curl -LsSf https://astral.sh/uv/install.sh | sh
    - export PATH="$HOME/.local/bin:$PATH"
  script:
    - uv run python -m build
  artifacts:
    paths:
      - dist/*
```

---

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: uv-sync
        name: Sync dependencies
        entry: uv sync --frozen
        language: system
        pass_filenames: false
        stages: [commit]
      
      - id: uv-lint
        name: Lint
        entry: uv run ruff check .
        language: system
        pass_filenames: true
        types: [python]
      
      - id: uv-format
        name: Format
        entry: uv run ruff format .
        language: system
        pass_filenames: true
        types: [python]
      
      - id: uv-type
        name: Type check
        entry: uv run mypy .
        language: system
        pass_filenames: true
        types: [python]
```

**Install pre-commit:**
```bash
uv add --dev pre-commit
uv run pre-commit install
```

---

## Everyday Tasks

### Quick Script

```bash
# Run a quick Python script
uv run python -c "import requests; print(requests.get('https://api.github.com').json())"

# Or with a file
cat > quick.py << 'EOF'
import requests
response = requests.get('https://api.github.com/users/octocat')
print(response.json()['name'])
EOF
uv run python quick.py
```

---

### Virtual Environment for Experimentation

```bash
# Quick experiment
uv venv experiment
uv venv --activate experiment  # Rarely needed
uv pip install numpy pandas matplotlib
uv run python -c "import numpy as np; print(np.random.rand(5,5))"

# Clean up
uv venv --remove experiment
```

---

### Checking Package Info

```bash
# Check what's installed
uv pip list

# Check specific package version
uv pip show requests

# Check outdated packages
uv pip list --outdated

# Upgrade specific package
uv pip install --upgrade requests

# Search for packages
uv pip search flask
```

---

### Managing Multiple Projects

```bash
# Project 1
cd project1
uv add requests
uv sync

# Project 2 (UV keeps them separate)
cd ../project2
uv add pandas
uv sync

# Switch back to project 1
cd ../project1
uv run python script.py  # Uses project1's dependencies
```

---

### Updating UV Itself

```bash
# Check current version
uv --version

# Update UV
uv self update

# Or reinstall
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### Cleaning Up

```bash
# Remove project dependencies
cd my-project
rm -rf .venv uv.lock

# Or keep lockfile, just remove venv
rm -rf .venv

# Clear UV cache (if needed)
uv cache clear --all

# Remove old Python versions
uv python list
uv python remove 3.9.5
```

---

## Migration Examples

### From pip + requirements.txt

**Before:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python script.py
```

**After:**
```bash
uv pip install -r requirements.txt
uv run python script.py
```

---

### From poetry

**Before:**
```bash
poetry new myproject
cd myproject
poetry add requests
poetry install
poetry run python script.py
```

**After:**
```bash
uv init myproject
cd myproject
uv add requests
uv sync
uv run python script.py
```

**Converting pyproject.toml:**
```toml
# Poetry's pyproject.toml
[tool.poetry]
name = "myproject"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"

[tool.poetry.dev-dependencies]
pytest = "^7.0"

# UV-compatible pyproject.toml
[project]
name = "myproject"
version = "0.1.0"
requires-python = ">=3.8"
dependencies = ["requests>=2.28.0"]

[project.optional-dependencies]
dev = ["pytest>=7.0"]
```

---

### From pipenv

**Before:**
```bash
pipenv install requests
pipenv run python script.py
```

**After:**
```bash
uv init myproject
cd myproject
uv add requests
uv sync
uv run python script.py
```

---

## Cheat Sheet

### Common Command Patterns

| Task | Command |
|------|---------|
| Create project | `uv init` |
| Add dependency | `uv add package` |
| Add dev dependency | `uv add --dev package` |
| Install all | `uv sync` |
| Run script | `uv run python script.py` |
| Run tests | `uv run pytest` |
| Lock dependencies | `uv lock` |
| Update dependencies | `uv lock --upgrade` |
| Create venv | `uv venv` |
| Install Python | `uv python install 3.11.8` |

### Speed Comparison Cheat Sheet

| Command | pip | UV | Faster? |
|---------|-----|----|---------|
| Install package | `pip install pkg` | `uv pip install pkg` | ✅ 10-100x |
| Install from reqs | `pip install -r r.txt` | `uv pip install -r r.txt` | ✅ 10-100x |
| Create venv | `python -m venv .venv` | `uv venv` | ✅ 20x |
| Run in venv | `source .venv/bin/activate && python s.py` | `uv run python s.py` | ✅ Instant |
| Freeze | `pip freeze` | `uv pip freeze` | ✅ 10x |

---

## Final Tips

1. **Just try it** - Run `uv --version` or `uv pip install package` right now
2. **Replace pip** - Every time you type `pip`, type `uv pip` instead
3. **Use projects** - `uv init` for any new Python work
4. **Embrace `uv run`** - No more `source activate`
5. **Lock dependencies** - `uv lock` for reproducibility

**Remember: The only thing you'll regret about UV is not trying it sooner.**
