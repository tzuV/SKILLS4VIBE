---
name: clean-lean-coder
description: Enforce clean code principles, refactor code, generate boilerplate, and provide real-time code reviews for maintainable, modular software. Use when user asks to refactor, review code, improve structure, enforce best practices, or generate boilerplate.
---

# Clean & Lean Coder

## Quick Start

**When triggered**, automatically:
1. Scan code for violations (magic numbers, long functions, nested conditionals)
2. Suggest specific refactors with before/after examples
3. Generate missing boilerplate (utils/, config/, tests/)

**Example triggers**: 
- "Refactor this function"
- "Review my code for best practices"
- "How should I structure this project?"
- "Generate a utils file for these helpers"

## Core Workflows

### 1. Code Refactoring
- [ ] Flag functions > 20 lines or with > 3 responsibilities
- [ ] Identify hardcoded values → move to `config/`
- [ ] Replace nested if/else with guard clauses or early returns
- [ ] Extract repeated logic to `utils/`
- [ ] Simplify complex expressions with helper functions

### 2. Boilerplate Generation
- [ ] Create `utils/` with common helpers and imports
- [ ] Generate `config/` for constants and environment variables
- [ ] Scaffold test stubs for `utils/` functions
- [ ] Provide feature templates (API clients, data processors)

### 3. Real-Time Code Review
- [ ] Check against system prompt rules (hardcoded strings, magic numbers)
- [ ] Suggest improvements with concrete before/after examples
- [ ] Enforce consistent naming conventions and import order
- [ ] Validate file organization ("This belongs in utils/")

### 4. Best Practice Enforcement
- [ ] DRY, KISS, YAGNI violation detection
- [ ] SOLID principle checks (Single Responsibility, Open/Closed)
- [ ] Pure function validation (no side effects)
- [ ] Error handling patterns (custom exceptions, fail-fast)

## Standard Project Structure
```
project/
├── src/           # Core application logic
├── utils/         # Reusable helper functions
├── config/        # Constants and configuration
├── tests/         # Unit and integration tests
└── scripts/       # Utility scripts
```

## When to Use
- User pastes code and asks for improvement
- User wants to add a new feature with proper structure
- User asks for code review
- User wants to refactor existing code
- User needs boilerplate generated

## Advanced Features
See [REFERENCE.md](REFERENCE.md) for detailed principles and [EXAMPLES.md](EXAMPLES.md) for before/after code examples.
