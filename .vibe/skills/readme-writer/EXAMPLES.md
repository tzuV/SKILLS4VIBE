# Examples

## Example 1: Generate README for Python Project

**User Request:**
> "Create a README for this Python project"

**Context:**
- Project has `pyproject.toml` with name="my-package", version="0.1.0", description="A helpful utility library"
- Main module is in `src/my_package/__init__.py`
- Tests in `tests/` directory
- MIT license

**Process:**
1. Read `pyproject.toml` to extract metadata
2. Scan directory structure
3. Identify Python project with tests
4. Generate appropriate README

**Output:**
```markdown
# My Package

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/my-package)](https://pypi.org/project/my-package/)

A helpful utility library for common development tasks.

## Installation

```bash
# From PyPI
pip install my-package

# From source
pip install -e .
```

## Usage

```python
from my_package import main_function

result = main_function(arg1, arg2)
print(result)
```

## Development

```bash
# Clone the repository
git clone https://github.com/user/my-package.git
cd my-package

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

## Example 2: Generate README for Node.js Project

**User Request:**
> "Write a README for my Node.js package"

**Context:**
- `package.json` with name="my-node-package", version="1.0.0"
- Main file: `index.js`
- Scripts: `start`, `test`, `build`
- Dependencies: `express`, `lodash`

**Output:**
```markdown
# My Node Package

[![Node.js](https://img.shields.io/badge/node-%3E%3D14.0.0-blue.svg)](https://nodejs.org/)
[![npm version](https://img.shields.io/npm/v/my-node-package)](https://www.npmjs.com/package/my-node-package)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Node.js package for [brief description].

## Installation

```bash
npm install my-node-package
```

## Usage

```javascript
const { myFunction } = require('my-node-package');

const result = myFunction(input);
```

## Scripts

```bash
# Start the application
npm start

# Run tests
npm test

# Build the package
npm run build
```

## License

MIT
```

---

## Example 3: Markdown Table Formatting

**User Request:**
> "Format this as a markdown table: Name: Alice, Role: Developer, Experience: 5 years; Name: Bob, Role: Designer, Experience: 3 years"

**Output:**
```markdown
| Name  | Role     | Experience |
|-------|----------|------------|
| Alice | Developer | 5 years    |
| Bob   | Designer  | 3 years    |
```

---

## Example 4: Codebase Summarization

**User Request:**
> "Summarize the structure of this project"

**Context:**
```
project/
├── src/
│   ├── main.py
│   ├── utils/
│   │   ├── helpers.py
│   │   └── validators.py
│   └── models/
│       ├── user.py
│       └── post.py
├── tests/
│   ├── test_main.py
│   └── test_utils/
│       └── test_helpers.py
├── docs/
│   └── api.md
├── README.md
└── pyproject.toml
```

**Output:**
```markdown
## Codebase Structure

```
project/
├── src/
│   ├── main.py              # Entry point, CLI interface
│   ├── utils/
│   │   ├── helpers.py       # Common utility functions (12 functions)
│   │   └── validators.py    # Input validation logic (5 validators)
│   └── models/
│       ├── user.py          # User data model and business logic
│       └── post.py          # Post/content model
├── tests/
│   ├── test_main.py         # Main module tests (25 tests)
│   └── test_utils/
│       └── test_helpers.py  # Helper function tests (18 tests)
├── docs/
│   └── api.md               # API documentation
├── README.md
└── pyproject.toml          # Project configuration, dependencies
```

**Key Modules:**
- `src/main.py`: CLI entry point with argument parsing
- `src/utils/helpers.py`: Shared utility functions
- `src/models/user.py`: Core domain model

**Test Coverage:** 95% (43/45 functions tested)
```

---

## Example 5: Step-by-Step Tutorial

**User Request:**
> "Create a tutorial for setting up and running this React app"

**Context:**
- React project with Vite
- Requires Node.js 18+
- Has development and production scripts

**Output:**
```markdown
## Getting Started with My React App

### Prerequisites

- [Node.js](https://nodejs.org/) 18.0.0 or later
- npm or yarn (included with Node.js)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/user/my-react-app.git
   cd my-react-app
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Optional: Install yarn (if preferred):**
   ```bash
   npm install -g yarn
   yarn install
   ```

### Running the App

1. **Development server:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   
   Open [http://localhost:5173](http://localhost:5173) in your browser.

2. **Production build:**
   ```bash
   npm run build
   npm run preview
   ```

### Project Structure

```
my-react-app/
├── public/          # Static files
├── src/
│   ├── assets/      # Images, styles
│   ├── components/  # React components
│   ├── pages/       # Page components
│   ├── App.jsx      # Main app component
│   └── main.jsx     # Entry point
└── vite.config.js   # Vite configuration
```

### Common Issues

**Error: Port already in use**
```bash
# Either change the port in vite.config.js
# Or kill the process using the port:
npx kill-port 5173
```

**Error: Missing dependencies**
```bash
npm install
```
```

---

## Example 6: Update Existing README

**User Request:**
> "Update the README to add a Contributing section"

**Current README:**
```markdown
# My Project

A simple project.

## Installation

pip install .

## Usage

python -m my_project
```

**Output (added section):**
```markdown
# My Project

A simple project.

## Installation

pip install .

## Usage

python -m my_project

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/user/my-project.git
cd my-project
pip install -e ".[dev]"
```
```

---

## Example 7: Format Data as Definition List

**User Request:**
> "Format these terms as a definition list: CLI, API, SDK"

**Output:**
```markdown
CLI
: Command Line Interface - A text-based interface for interacting with software

API
: Application Programming Interface - A set of protocols and tools for building software applications

SDK
: Software Development Kit - A collection of software development tools in one installable package
```
