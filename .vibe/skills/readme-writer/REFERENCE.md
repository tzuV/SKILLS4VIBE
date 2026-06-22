# Advanced Features & Reference

## README Section Guidelines

### Required Sections (Always Include)

#### 1. Title (H1)
- Use the exact project name from configuration files
- Capitalize properly (Title Case or as specified in project)
- Keep it simple and direct

**Format:**
```markdown
# Project Name
```

#### 2. Description
- First paragraph after title/badges
- 1-3 sentences maximum
- Explain what the project does, not how it does it
- Use present tense, active voice

**Good:**
```markdown
A Python library for parsing and validating email addresses with support for international domains.
```

**Avoid:**
```markdown
This is a project that I created to help with email parsing. It's really useful for... (too verbose)
```

#### 3. Installation
- Always include this section
- Show the simplest/most common installation method first
- Include alternatives (from source, different package managers)

**Format:**
```markdown
## Installation

```bash
# Recommended
pip install package-name

# From source
pip install -e git+https://github.com/user/repo.git
```
```

#### 4. Usage
- Minimum one working example
- Show the simplest possible usage first
- Include code blocks with proper language tags
- For libraries: show import and basic function call
- For applications: show how to run it

**Format:**
```markdown
## Usage

```python
from package import main_function

result = main_function('input')
print(result)
```
```

### Conditional Sections

#### Badges
Include badges for:
- **Language/Version:** Python, Node.js, Java, etc.
- **Package Registry:** PyPI, npm, Maven, etc.
- **CI/CD:** GitHub Actions, Travis CI, CircleCI
- **Test Coverage:** Coveralls, Codecov
- **License:** MIT, Apache, GPL
- **Other:** Downloads, Dependencies, etc.

**Format:**
```markdown
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/package-name)](https://pypi.org/project/package-name/)
[![CI Status](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/user/repo/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
```

**Badge Services:**
- [Shields.io](https://shields.io/) - Most comprehensive
- [Badgen.net](https://badgen.net/) - Simpler, faster

#### Table of Contents
- Include if README exceeds 100 lines
- Link to all H2 sections
- Use consistent naming with section headers

**Format:**
```markdown
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
```

#### Configuration
- Include if the project has configurable options
- Show default configuration
- Explain each option

**Format:**
```markdown
## Configuration

Create a `config.json` file:

```json
{
  "option1": "default_value",
  "option2": true
}
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| option1 | string | `"default"` | Controls behavior X |
| option2 | boolean | `true` | Enables feature Y |
```

#### API Reference
- Include for library/package projects
- Document public functions/classes
- Group related functionality

**Format:**
```markdown
## API Reference

### ClassName

#### `method_name(parameters)`

- **Parameters:**
  - `param1` (type): Description
  - `param2` (type, optional): Description. Default: `value`

- **Returns:** (type) Description

- **Raises:**
  - `ValueError`: If input is invalid
  - `TypeError`: If types don't match

**Example:**
```python
from package import ClassName

obj = ClassName()
result = obj.method_name(param1, param2='value')
```
```

#### Contributing
- Include for open-source projects
- Specify contribution requirements
- Include development setup

**Format:**
```markdown
## Contributing

Contributions are welcome!

### Development Setup

```bash
git clone https://github.com/user/repo.git
cd repo
pip install -e ".[dev]"
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a Pull Request

### Coding Standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python
- Include type hints
- Add docstrings
- Keep line length under 88 characters
```

#### Tests
- Include if project has tests
- Show how to run tests
- Mention test coverage if known

**Format:**
```markdown
## Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=package

# Run specific test
pytest tests/test_module.py::test_function
```

**Coverage:** 95% (120/126 lines)
```

#### License
- Always include
- Use SPDX identifier if standard license
- Link to LICENSE file if custom

**Format:**
```markdown
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Or simply:
```markdown
MIT
```

### Project Type Specifics

#### Python Projects
- Detect from: `pyproject.toml`, `setup.py`, `setup.cfg`, `*.py` files
- Installation: `pip install`
- Testing: `pytest`
- Quality: `black`, `flake8`, `mypy`

**Common Files:**
```
project/
├── pyproject.toml      # Modern project configuration
├── setup.py            # Legacy project configuration
├── setup.cfg           # Legacy project configuration
├── requirements.txt    # Dependencies
├── src/                # Source code (or project root)
│   └── package_name/
│       ├── __init__.py
│       └── ...
├── tests/              # Tests
├── docs/               # Documentation
└── README.md
```

#### Node.js Projects
- Detect from: `package.json`, `*.js`, `*.ts` files
- Installation: `npm install` or `yarn install`
- Testing: `npm test`, `jest`
- Bundling: `webpack`, `vite`, `rollup`

**Common Files:**
```
project/
├── package.json        # Project configuration
├── package-lock.json   # Dependency lock file
├── node_modules/      # Dependencies (not in repo)
├── src/                # Source code
│   └── index.js        # Entry point
├── test/ or __tests__/ # Tests
├── dist/               # Built output
└── README.md
```

#### Java Projects
- Detect from: `pom.xml`, `build.gradle`, `*.java` files
- Installation: `mvn install`, `gradle build`
- Testing: `mvn test`

**Common Files:**
```
project/
├── pom.xml             # Maven configuration
├── src/
│   ├── main/
│   │   └── java/       # Source code
│   └── test/
│       └── java/       # Tests
└── README.md
```

#### Go Projects
- Detect from: `go.mod`, `*.go` files
- Installation: `go install`
- Testing: `go test`

**Common Files:**
```
project/
├── go.mod              # Module definition
├── go.sum              # Dependency checksums
├── cmd/                # Main applications
├── pkg/                # Library code
├── internal/           # Internal packages
└── README.md
```

#### Rust Projects
- Detect from: `Cargo.toml`, `*.rs` files
- Installation: `cargo install`
- Testing: `cargo test`

**Common Files:**
```
project/
├── Cargo.toml          # Project configuration
├── Cargo.lock          # Dependency lock file
├── src/
│   ├── main.rs         # Binary entry point
│   └── lib.rs          # Library entry point
├── tests/              # Integration tests
└── README.md
```

## Markdown Formatting Reference

### Tables

**Basic Table:**
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

**With Alignment:**
```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L1   | C1     | R1    |
| L2   | C2     | R2    |
```

**From CSV Data:**
```
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
```

**Output:**
```markdown
| Name  | Age | City       |
|-------|-----|------------|
| Alice | 30  | New York   |
| Bob   | 25  | Los Angeles|
```

### Code Blocks

**With Language Tag:**
````markdown
```python
def hello():
    return "World"
```
````

**Multi-line with Empty Lines:**
````markdown
```bash
# This is a comment

# This is another line with empty line above
```
````

**Without Language Tag:**
```markdown
```
Plain text or unknown language
```
```

### Lists

**Bullet List:**
```markdown
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3
```

**Numbered List:**
```markdown
1. First item
2. Second item
3. Third item
```

**Checklist:**
```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

**Definition List:**
```markdown
Term 1
: Definition for term 1

Term 2
: Definition for term 2
```

### Links

**Inline Link:**
```markdown
[Link Text](https://example.com)
```

**Reference Link:**
```markdown
[Link Text][id]

[id]: https://example.com "Optional title"
```

**Relative Link:**
```markdown
[API Docs](./docs/api.md)
[Parent Directory](../README.md)
```

**Email Link:**
```markdown
[Email Me](mailto:user@example.com)
```

### Images

**Basic Image:**
```markdown
![Alt Text](path/to/image.png)
```

**With Title:**
```markdown
![Alt Text](path/to/image.png "Image Title")
```

**Relative Path:**
```markdown
![Logo](./assets/logo.png)
```

**From URL:**
```markdown
![Screenshot](https://example.com/screenshot.png)
```

### Blockquotes

**Single Line:**
```markdown
> This is a quote
```

**Multi-line:**
```markdown
> This is a multi-line quote.
> It can span multiple lines.
> Each line starts with >.
```

**Nested Quotes:**
```markdown
> First level
> > Second level
> > > Third level
```

### Horizontal Rules

```markdown
---

or

***

or

___
```

### HTML in Markdown

**When to Use:**
- For elements not supported in Markdown (tables with colspan, etc.)
- For advanced styling

**Example:**
```markdown
<div align="center">
  <img src="./logo.png" alt="Logo" width="200">
</div>
```

## Language-Specific Templates

### Python README Template

```markdown
# {{ package_name }}

[![Python {{ python_version }}](https://img.shields.io/badge/python-{{ python_version }}-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/{{ package_name }})](https://pypi.org/project/{{ package_name }}/)
[![License: {{ license }}](https://img.shields.io/badge/license-{{ license }}-green.svg)](LICENSE)

{{ description }}

## Installation

```bash
pip install {{ package_name }}
```

## Usage

```python
from {{ package_name }} import {{ main_export }}

{{ usage_example }}
```

## Development

```bash
git clone https://github.com/{{ user }}/{{ repo }}.git
cd {{ repo }}
pip install -e ".[dev]"
pytest
```

## License

{{ license }}
```

### Node.js README Template

```markdown
# {{ package_name }}

[![Node.js {{ node_version }}](https://img.shields.io/badge/node-%3E%3D{{ node_version }}-blue.svg)](https://nodejs.org/)
[![npm version](https://img.shields.io/npm/v/{{ package_name }})](https://www.npmjs.com/package/{{ package_name }})
[![License: {{ license }}](https://img.shields.io/badge/license-{{ license }}-green.svg)](LICENSE)

{{ description }}

## Installation

```bash
npm install {{ package_name }}
```

## Usage

```javascript
const { {{ main_export }} } = require('{{ package_name }}');

{{ usage_example }}
```

## Scripts

```bash
npm run {{ scripts }}
```

## License

{{ license }}
```

## Badge References

### Language Badges

| Language | Badge | URL |
|----------|-------|-----|
| Python 3.8+ | `[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)` | https://www.python.org/downloads/ |
| Node.js | `[![Node.js](https://img.shields.io/badge/node-%3E%3D14.0.0-blue.svg)](https://nodejs.org/)` | https://nodejs.org/ |
| Java | `[![Java](https://img.shields.io/badge/java-%3E%3D11-orange.svg)](https://www.java.com/)` | https://www.java.com/ |
| Go | `[![Go](https://img.shields.io/badge/go-1.18+-blue.svg)](https://go.dev/)` | https://go.dev/ |
| Rust | `[![Rust](https://img.shields.io/badge/rust-1.60+-orange.svg)](https://www.rust-lang.org/)` | https://www.rust-lang.org/ |

### Package Registry Badges

| Registry | Badge | URL |
|----------|-------|-----|
| PyPI | `[![PyPI version](https://img.shields.io/pypi/v/package-name)](https://pypi.org/project/package-name/)` | https://pypi.org/project/package-name/ |
| npm | `[![npm version](https://img.shields.io/npm/v/package-name)](https://www.npmjs.com/package/package-name)` | https://www.npmjs.com/package/package-name |
| Maven | `[![Maven Central](https://img.shields.io/maven-central/v/group_id/artifact_id)](https://search.maven.org/artifact/group_id/artifact_id)` | https://search.maven.org/artifact/group_id/artifact_id |

### CI/CD Badges

| Service | Badge | URL |
|---------|-------|-----|
| GitHub Actions | `[![CI](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/user/repo/actions)` | https://github.com/user/repo/actions |
| Travis CI | `[![Build Status](https://travis-ci.org/user/repo.svg?branch=main)](https://travis-ci.org/user/repo)` | https://travis-ci.org/user/repo |
| CircleCI | `[![CircleCI](https://circleci.com/gh/user/repo/tree/main.svg?style=shield)](https://circleci.com/gh/user/repo/tree/main)` | https://circleci.com/gh/user/repo |

### License Badges

| License | Badge | SPDX |
|---------|-------|------|
| MIT | `[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)` | MIT |
| Apache 2.0 | `[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)` | Apache-2.0 |
| GPLv3 | `[![License: GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)` | GPL-3.0 |
| BSD 3-Clause | `[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](LICENSE)` | BSD-3-Clause |

## File Detection Patterns

### Project Configuration Files

| File | Language/Framework |
|------|-------------------|
| `pyproject.toml` | Python (PEP 621) |
| `setup.py` | Python (Legacy) |
| `package.json` | Node.js |
| `pom.xml` | Java (Maven) |
| `build.gradle` | Java (Gradle) |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `composer.json` | PHP |
| `Gemfile` | Ruby |
| `Makefile` | C/C++/Make |
| `requirements.txt` | Python (Dependencies) |

### Framework Indicators

| File/Directory | Framework |
|----------------|-----------|
| `next.config.js` | Next.js |
| `vite.config.js` | Vite |
| `webpack.config.js` | Webpack |
| `angular.json` | Angular |
| `vue.config.js` | Vue.js |
| `tailwind.config.js` | Tailwind CSS |
| `.django/` | Django |
| `.flask/` | Flask |
| `prisma/` | Prisma |
| `dart_tool/` | Dart/Flutter |

### Test Framework Indicators

| File | Framework |
|------|-----------|
| `pytest.ini` | pytest |
| `jest.config.js` | Jest |
| `karma.conf.js` | Karma |
| `phpunit.xml` | PHPUnit |
| `spec/` directory | RSpec |
| `test_*.py` | Python unittest/pytest |
| `*.test.js` | Node.js test files |

## Common Commands by Language

### Python

```bash
# Install package
pip install package-name

# Install from source
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
pytest --cov=package

# Format code
black .

# Lint
flake8
mypy .

# Type checking
mypy .
```

### Node.js

```bash
# Install package
npm install package-name

# Install all dependencies
npm install

# Run script
npm run script-name

# Run tests
npm test

# Start development server
npm start

# Build for production
npm run build

# Type checking
tsc --noEmit
```

### Go

```bash
# Install package
go install github.com/user/repo@latest

# Get dependencies
go get ./...

# Build
go build

# Run
go run main.go

# Run tests
go test ./...

# Format code
gofmt -w .
```

### Rust

```bash
# Install package
cargo install package-name

# Build
cargo build

# Run
cargo run

# Run tests
cargo test

# Check formatting
cargo fmt --check

# Apply formatting
cargo fmt

# Clippy linting
cargo clippy
```
