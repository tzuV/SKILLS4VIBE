# Clean & Lean Coder - Reference Guide

## Core Principles

### 1. SOLID Principles (Object-Oriented Design)

| Principle | Description | Code Example |
|-----------|-------------|--------------|
| **Single Responsibility** | A class/function should have only one reason to change | One function handles validation, another handles DB operations |
| **Open/Closed** | Open for extension, closed for modification | Use abstract base classes or interfaces |
| **Liskov Substitution** | Subtypes must be substitutable for their base types | Square is not a Rectangle (violates LSP) |
| **Interface Segregation** | Clients shouldn't be forced to depend on unused interfaces | Split large interfaces into smaller, specific ones |
| **Dependency Inversion** | Depend on abstractions, not concretions | Inject dependencies via interfaces |

### 2. Lean Code Principles

#### DRY (Don't Repeat Yourself)
- **Violation**: Same validation logic in 3 different places
- **Fix**: Extract to `utils/validators.py` or `validators.js`
- **Exception**: Don't abstract if it's only used twice and unlikely to change

#### KISS (Keep It Simple, Stupid)
- **Violation**: Over-engineered factory pattern for 2 subclasses
- **Fix**: Use simple conditional or dictionary mapping
- **Rule**: Favor simplicity over cleverness

#### YAGNI (You Aren't Gonna Need It)
- **Violation**: Building a generic cache system when only one cache is needed
- **Fix**: Implement only what's needed now
- **Rule**: Don't build for hypothetical future requirements

### 3. Clean Code Guidelines (Robert C. Martin)

#### Functions
- **Max length**: 20 lines (soft limit)
- **Max responsibilities**: 1 (Single Responsibility)
- **Naming**: Use intention-revealing names
- **Parameters**: < 4 (ideal: 0-2)
- **Side effects**: Minimize (prefer pure functions)

#### Variables
- **Naming**: `daily_mood_score` > `x` or `data`
- **Scope**: Declare as close to use as possible
- **Magic numbers**: Replace with named constants
- **Hardcoded strings**: Move to config or constants

#### Conditionals
- **Nesting depth**: < 3 levels
- **Prefer**: Guard clauses over nested if/else
- **Pattern**: Early returns for error cases
- **Avoid**: Deeply nested ternary operators

### 4. File Organization

#### Standard Structure
```
project/
├── src/
│   ├── core/          # Domain logic
│   ├── adapters/      # External integrations (APIs, DB)
│   └── models/        # Data structures
├── utils/
│   ├── helpers.py     # Pure utility functions
│   ├── validators.py  # Input validation
│   └── __init__.py    # Exports
├── config/
│   ├── settings.py    # Application settings
│   ├── constants.py   # Magic numbers, strings
│   └── secrets.py     # API keys (gitignored)
├── tests/
│   ├── unit/          # Unit tests
│   └── integration/   # Integration tests
└── scripts/
    └── setup.py       # Project setup scripts
```

#### File Naming Conventions
- **Python**: `snake_case.py`
- **JavaScript**: `camelCase.js` or `kebab-case.js`
- **Tests**: `test_<module>.py` or `<module>.test.js`
- **Configs**: `settings.py`, `constants.py`
- **Utils**: `helpers.py`, `validators.py`, `formatters.py`

### 5. Configuration Management

#### Environment Variables (12-Factor App)
- **Rule**: All config in environment variables
- **Pattern**: Use `.env` files for development
- **Never**: Commit secrets to git
- **Libraries**: `python-dotenv`, `dotenv` (JS)

#### Config File Structure
```python
# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY = os.getenv("API_KEY")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

settings = Settings()
```

### 6. Error Handling

#### Custom Exceptions
```python
# src/exceptions.py
class ValidationError(Exception):
    """Raised when input validation fails"""
    pass

class APIError(Exception):
    """Raised when API request fails"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
```

#### Fail-Fast Pattern
- **Rule**: Validate inputs at function entry
- **Pattern**: Raise exceptions immediately on invalid input
- **Avoid**: Silent failures or null returns

### 7. Testing Best Practices

#### Unit Test Structure (AAA Pattern)
```python
# tests/unit/test_utils.py
def test_calculate_discount():
    # Arrange
    price = 100
    discount = 0.2
    
    # Act
    result = calculate_discount(price, discount)
    
    # Assert
    assert result == 80
```

#### Test Coverage
- **Target**: 80-90% coverage for critical paths
- **Focus**: Test edge cases, not just happy paths
- **Avoid**: Testing implementation details

### 8. Linting & Formatting

#### Python
- **Linter**: `flake8` or `pylint`
- **Formatter**: `black` or `autopep8`
- **Type checker**: `mypy`
- **Config**: `.flake8`, `pyproject.toml`

#### JavaScript
- **Linter**: `ESLint`
- **Formatter**: `Prettier`
- **Type checker**: `TypeScript` or `JSDoc`
- **Config**: `.eslintrc.js`, `.prettierrc`

### 9. Performance vs. Readability Trade-offs

#### When to Optimize
- **Do optimize**: Hot code paths (measured with profiling)
- **Don't optimize**: Code that runs once at startup
- **Rule**: Measure before optimizing

#### Python-Specific
- **Use**: List comprehensions for simple transformations
- **Avoid**: Nested comprehensions (hard to read)
- **Use**: Built-ins (`map`, `filter`, `itertools`) when appropriate
- **Avoid**: Clever one-liners that sacrifice readability

#### JavaScript-Specific
- **Use**: `Array.map`, `Array.filter`, `Array.reduce`
- **Avoid**: Deeply chained array methods
- **Use**: Destructuring for clarity
- **Avoid**: Excessive destructuring that obscures intent

### 10. Code Review Checklist

#### Before Submitting Code
- [ ] All magic numbers replaced with named constants
- [ ] All hardcoded strings moved to config
- [ ] Functions < 20 lines with single responsibility
- [ ] Nesting depth < 3 levels
- [ ] Variable names are intention-revealing
- [ ] No repeated logic (DRY)
- [ ] All imports are used
- [ ] Error handling with custom exceptions where appropriate
- [ ] Tests cover new functionality
- [ ] Linter/formatter passes

#### During Code Review
- [ ] Check for system prompt rule violations
- [ ] Verify file organization (code in right location)
- [ ] Ensure consistent naming conventions
- [ ] Validate import order (grouped, alphabetical)
- [ ] Check for potential side effects
- [ ] Verify error messages are helpful

## Recommended Tools

### Python
- **Linter**: `flake8`, `pylint`
- **Formatter**: `black`, `autopep8`
- **Type checker**: `mypy`
- **Testing**: `pytest`, `unittest`
- **Env vars**: `python-dotenv`

### JavaScript
- **Linter**: `ESLint`
- **Formatter**: `Prettier`
- **Type checker**: `TypeScript`
- **Testing**: `Jest`, `Mocha`
- **Env vars**: `dotenv`

### General
- **Git hooks**: `pre-commit`
- **CI/CD**: `GitHub Actions`, `GitLab CI`
- **Profiling**: `cProfile` (Python), `node --prof` (JS)

## External References

- [PEP 8 - Python Style Guide](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- [SOLID Principles (Wikipedia)](https://en.wikipedia.org/wiki/SOLID)
- [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- [12-Factor App](https://12factor.net/)
