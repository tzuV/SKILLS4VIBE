---
name: test-generator
description: Scan repositories and generate or update unit/integration tests for untested components, including API endpoints, database interactions, and security validations. Use when user asks to add tests, improve test coverage, generate missing tests, or ensure all components are tested.
---

# Test Generator

## Quick Start

User says: *"Add tests for my API"* or *"Improve test coverage"*

1. **Scan** the repository structure
2. **Detect** language, framework, and existing test patterns
3. **Identify** untested components (functions, classes, API routes, DB models)
4. **Generate** appropriate test files with meaningful assertions
5. **Update** existing incomplete tests
6. **Optionally** run tests and report coverage

## Workflows

### Full Repository Scan
```
User: "Generate tests for this entire codebase"
→ Scan all source files
→ Identify all exportable functions/classes
→ Cross-reference with existing test files
→ Generate test files for gaps
→ Report summary
```

### Targeted Test Generation
```
User: "Add tests for src/api/users.py"
→ Analyze the specific file
→ Detect its dependencies (DB, external APIs, services)
→ Generate comprehensive tests including:
  - Unit tests for pure functions
  - Integration tests for API endpoints
  - Mock tests for external dependencies
→ Save to appropriate test directory
```

### Test Update Mode
```
User: "Improve the tests in tests/api/test_users.py"
→ Read existing test file
→ Identify missing test cases
→ Update file with new test cases
→ Preserve existing test style
```

## Language & Framework Detection

**Auto-detect by priority:**

| Language | Frameworks (in order) | Test File Patterns |
|----------|------------------------|-------------------|
| Python | pytest, unittest | `test_*.py`, `*_test.py`, `tests/` |
| JavaScript | Jest, Vitest, Mocha | `*.test.js`, `*.spec.js`, `__tests__/` |
| TypeScript | Jest, Vitest | `*.test.ts`, `*.spec.ts` |
| Java | JUnit, TestNG | `*Test.java`, `test/` |
| Go | testing, Testify | `*_test.go` |
| Rust | rust-test | `tests/`, `*_test.rs` |
| C# | xUnit, NUnit | `*Test.cs`, `Tests/` |

**If undetected:** Ask user to specify or default to most common for language.

## Test Types Generated

### By Component Type

| Component | Test Type | What's Tested |
|-----------|-----------|---------------|
| Utility functions | Unit | Pure logic, edge cases, type safety |
| API endpoints | Integration | HTTP methods, status codes, request/response validation, auth |
| Database models | Unit + Integration | CRUD operations, queries, relationships, transactions |
| Services/Managers | Unit | Business logic, error handling, dependency calls (mocked) |
| Controllers | Integration | Route handling, middleware, request/response flow |
| Authentication | Security + Integration | Token validation, permission checks, rate limiting |
| External API calls | Unit (mocked) | Request formatting, response handling, error cases |

### Security Tests (when applicable)
- SQL injection attempts on DB queries
- XSS attempts on input validation
- Authentication bypass attempts
- Rate limiting validation
- Input sanitization checks

### Database Tests
- Connection establishment
- Query execution and results
- Transaction rollback
- Migration validity
- Data integrity constraints

## Test Quality Standards

**Every generated test must:**
- [ ] Have a clear, descriptive name (`test_get_user_returns_404_for_nonexistent_id`)
- [ ] Test one thing (single assertion where possible)
- [ ] Include both happy path and error cases
- [ ] Use proper setup/teardown (fixtures, beforeEach, etc.)
- [ ] Mock external dependencies
- [ ] Have reasonable timeouts
- [ ] Follow existing code style

**Avoid:**
- Tests that depend on external services (unless explicitly integration tests)
- Hardcoded values that will break (use test data builders)
- Tests that modify production data
- Flaky tests (random, timing-dependent)

## Generation Process

1. **Analyze Target Code**
   - Parse structure to identify functions, classes, methods
   - Extract signatures (parameters, return types)
   - Identify dependencies (imports, API calls, DB queries)

2. **Cross-Reference with Existing Tests**
   - Map which functions are already tested
   - Identify test coverage gaps
   - Note existing test patterns and style

3. **Generate Test Cases**
   - Happy path for each function
   - Edge cases (null, empty, boundary values)
   - Error cases (invalid input, exceptions)
   - For APIs: all HTTP methods, auth scenarios
   - For DB: CRUD operations, query validation

4. **Create Test Files**
   - Follow existing directory structure
   - Use detected test framework conventions
   - Add to existing test files when appropriate
   - Create new files when needed

5. **Offer Execution**
   - Ask: "Would you like me to run these tests?"
   - If yes: execute and report results
   - If failures: offer to fix tests or code

## Commands & Triggers

| User Input | Action |
|------------|--------|
| "add tests for [file/directory]" | Generate tests for specified target |
| "improve test coverage" | Scan repo, generate missing tests |
| "generate tests for all untested code" | Full scan and generate |
| "update tests in [file]" | Enhance existing test file |
| "write tests for the API" | Generate API endpoint tests |
| "test the database layer" | Generate DB model/operation tests |
| "add security tests" | Generate security-focused tests |
| "make sure everything is tested" | Full coverage analysis and test generation |

## Configuration

Users can create a `.testgenrc` file in repo root:

```yaml
# .testgenrc
framework: pytest  # Override auto-detection
min_coverage: 80   # Target coverage percentage
include:
  - src/**
  - lib/**
exclude:
  - generated/**
  - tests/**
test_timeout: 5000  # ms
mock_external: true # Auto-mock external API calls
```

## Example Output

**Input:** `src/utils/string_helpers.py`
```python
def sanitize_input(text: str) -> str:
    if not text:
        raise ValueError("Input cannot be empty")
    return text.replace("<script>", "").replace("</script>", "")

def generate_slug(text: str) -> str:
    return text.lower().replace(" ", "-")
```

**Generated:** `tests/test_string_helpers.py`
```python
import pytest
from src.utils.string_helpers import sanitize_input, generate_slug

class TestSanitizeInput:
    def test_removes_script_tags(self):
        assert sanitize_input("Hello<script>alert('xss')</script>") == "Helloalert('xss')"

    def test_empty_input_raises_error(self):
        with pytest.raises(ValueError, match="Input cannot be empty"):
            sanitize_input("")

    def test_plain_text_unchanged(self):
        assert sanitize_input("Hello World") == "Hello World"

class TestGenerateSlug:
    def test_converts_to_lowercase(self):
        assert generate_slug("Hello World") == "hello-world"

    def test_replaces_spaces_with_hyphens(self):
        assert generate_slug("Test Case") == "test-case"
```

See [TEST_PATTERNS.md](TEST_PATTERNS.md) for language-specific test patterns and examples.
