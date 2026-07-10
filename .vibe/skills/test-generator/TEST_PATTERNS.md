# Test Patterns by Language

Reference for language-specific test patterns, conventions, and examples.

---

## Python (pytest)

### File Structure
```
project/
├── src/
│   └── module/
│       └── file.py
└── tests/
    └── module/
        └── test_file.py
```

### Basic Test
```python
# tests/module/test_file.py
from src.module.file import function_to_test

def test_function_happy_path():
    result = function_to_test("input")
    assert result == "expected"

def test_function_edge_case():
    result = function_to_test("")
    assert result == "default"
```

### Parametrized Tests
```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("", ""),
])
def test_uppercase(input, expected):
    assert function_to_test(input) == expected
```

### Fixtures
```python
import pytest
from src.module.database import Database

@pytest.fixture
def db():
    db = Database(":memory:")
    db.setup()
    yield db
    db.teardown()

def test_query(db):
    result = db.query("SELECT 1")
    assert result == 1
```

### Mocking
```python
from unittest.mock import patch
from src.module.api import fetch_data

@patch("src.module.api.requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}

    result = fetch_data("https://api.example.com")
    assert result == {"key": "value"}
```

### API Testing (FastAPI example)
```python
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_create_item():
    response = client.post("/items/", json={"name": "Test"})
    assert response.status_code == 201
    assert "id" in response.json()
```

---

## JavaScript (Jest)

### File Structure
```
project/
├── src/
│   └── utils/
│       └── math.js
└── __tests__/
    └── utils/
        └── math.test.js
```

### Basic Test
```javascript
// math.test.js
const { add, subtract } = require('../../src/utils/math');

test('adds 1 + 2 to equal 3', () => {
  expect(add(1, 2)).toBe(3);
});

test('subtracts 2 - 1 to equal 1', () => {
  expect(subtract(2, 1)).toBe(1);
});
```

### Async Tests
```javascript
const { fetchUser } = require('../../src/api/user');

test('async fetch user', async () => {
  const user = await fetchUser(1);
  expect(user).toEqual({ id: 1, name: 'John' });
});
```

### Mocking
```javascript
const { getData } = require('../../src/api/data');
const axios = require('axios');

jest.mock('axios');

test('mocks axios get', async () => {
  axios.get.mockResolvedValue({ data: { key: 'value' } });

  const result = await getData();
  expect(result).toEqual({ key: 'value' });
  expect(axios.get).toHaveBeenCalledTimes(1);
});
```

### Snapshot Testing (React)
```javascript
import React from 'react';
import renderer from 'react-test-renderer';
import Component from '../../src/components/Component';

test('renders correctly', () => {
  const tree = renderer.create(<Component />).toJSON();
  expect(tree).toMatchSnapshot();
});
```

### API Testing (Express)
```javascript
const request = require('supertest');
const app = require('../../src/app');

describe('GET /api/users', () => {
  it('responds with JSON', async () => {
    const response = await request(app)
      .get('/api/users')
      .expect('Content-Type', /json/)
      .expect(200);

    expect(response.body).toBeInstanceOf(Array);
  });
});
```

---

## TypeScript (Jest)

### Basic Test with Types
```typescript
// math.test.ts
import { add, subtract } from '../../src/utils/math';

describe('Math operations', () => {
  test('adds two numbers', () => {
    expect(add(1, 2)).toBe(3);
  });

  test('throws on invalid input', () => {
    expect(() => add('1', 2)).toThrow('Invalid input');
  });
});
```

### Testing Interfaces
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function createUser(data: Partial<User>): User {
  return { id: Date.now(), name: '', email: '', ...data };
}

test('creates user with defaults', () => {
  const user = createUser({ name: 'John' });
  expect(user).toEqual({
    id: expect.any(Number),
    name: 'John',
    email: ''
  });
});
```

### Mocking Modules
```typescript
import { getConfig } from '../../src/config';
import { initializeApp } from '../../src/app';

jest.mock('../../src/config');

test('initializes app with config', () => {
  (getConfig as jest.Mock).mockReturnValue({ apiKey: 'test-key' });

  const app = initializeApp();
  expect(app.config.apiKey).toBe('test-key');
});
```

---

## Java (JUnit 5)

### File Structure
```
project/
├── src/
│   └── main/
│       └── java/
│           └── com/example/
│               └── Calculator.java
└── src/
    └── test/
        └── java/
            └── com/example/
                └── CalculatorTest.java
```

### Basic Test
```java
package com.example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class CalculatorTest {

    @Test
    void testAdd() {
        Calculator calculator = new Calculator();
        assertEquals(5, calculator.add(2, 3));
    }

    @Test
    void testSubtract() {
        Calculator calculator = new Calculator();
        assertEquals(1, calculator.subtract(3, 2));
    }
}
```

### Parameterized Tests
```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class StringUtilsTest {

    @ParameterizedTest
    @ValueSource(strings = {"", "  ", "\t"})
    void testIsBlank_BlankStrings(String input) {
        assertTrue(StringUtils.isBlank(input));
    }
}
```

### Mocking (Mockito)
```java
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Test
    void testGetUserById() {
        UserRepository mockRepo = mock(UserRepository.class);
        when(mockRepo.findById(1L)).thenReturn(new User(1L, "John"));

        UserService service = new UserService(mockRepo);
        User user = service.getUserById(1L);

        assertEquals("John", user.getName());
        verify(mockRepo, times(1)).findById(1L);
    }
}
```

### Exception Testing
```java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class ParserTest {

    @Test
    void testParse_InvalidInput_ThrowsException() {
        Parser parser = new Parser();

        Exception exception = assertThrows(ParseException.class, () -> {
            parser.parse("invalid");
        });

        assertEquals("Invalid input", exception.getMessage());
    }
}
```

---

## Go

### File Structure
```
project/
├── pkg/
│   └── utils/
│       └── math.go
└── pkg/
    └── utils/
        └── math_test.go
```

### Basic Test
```go
package utils

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    expected := 5

    if result != expected {
        t.Errorf("Expected %d, got %d", expected, result)
    }
}
```

### Table Tests
```go
func TestMultiply(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive numbers", 2, 3, 6},
        {"zero", 0, 5, 0},
        {"negative", -2, 3, -6},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Multiply(tt.a, tt.b); got != tt.expected {
                t.Errorf("Multiply(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.expected)
            }
        })
    }
}
```

### Mocking (with interfaces)
```go
type UserRepository interface {
    FindByID(id int) (*User, error)
}

type UserService struct {
    repo UserRepository
}

func TestGetUser(t *testing.T) {
    mockRepo := &MockUserRepo{}
    service := UserService{repo: mockRepo}

    user, err := service.GetUser(1)
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }

    if user.ID != 1 {
        t.Errorf("Expected ID 1, got %d", user.ID)
    }
}

type MockUserRepo struct{}

func (m *MockUserRepo) FindByID(id int) (*User, error) {
    return &User{ID: id, Name: "Test User"}, nil
}
```

### Sub-tests
```go
func TestHTTPHandler(t *testing.T) {
    t.Run("GET request", func(t *testing.T) {
        req := httptest.NewRequest("GET", "/hello", nil)
        w := httptest.NewRecorder()

        handler(w, req)

        if w.Code != http.StatusOK {
            t.Errorf("Expected status 200, got %d", w.Code)
        }
    })

    t.Run("POST request", func(t *testing.T) {
        // Test POST logic
    })
}
```

---

## Rust

### File Structure
```
project/
├── src/
│   └── lib.rs
└── tests/
    └── integration_test.rs
```

### Unit Tests (in same file)
```rust
// src/lib.rs
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add(-2, 3), 1);
    }
}
```

### Integration Tests
```rust
// tests/integration_test.rs
use my_crate::add;

#[test]
fn test_add_from_outside() {
    assert_eq!(add(10, 20), 30);
}
```

### Result Testing
```rust
#[test]
fn test_divide() {
    assert_eq!(divide(10, 2), Ok(5));
    assert_eq!(divide(10, 0), Err("division by zero"));
}

fn divide(a: i32, b: i32) -> Result<i32, &'static str> {
    if b == 0 {
        Err("division by zero")
    } else {
        Ok(a / b)
    }
}
```

---

## C#

### File Structure
```
project/
├── src/
│   └── MyApp/
│       └── Services/
│           └── Calculator.cs
└── tests/
    └── MyApp.Tests/
        └── Services/
            └── CalculatorTests.cs
```

### Basic Test (xUnit)
```csharp
using Xunit;

namespace MyApp.Tests.Services
{
    public class CalculatorTests
    {
        [Fact]
        public void Add_TwoNumbers_ReturnsSum()
        {
            var calculator = new Calculator();
            var result = calculator.Add(2, 3);

            Assert.Equal(5, result);
        }

        [Theory]
        [InlineData(1, 1, 2)]
        [InlineData(0, 0, 0)]
        [InlineData(-1, 1, 0)]
        public void Add_MultipleInputs_ReturnsCorrectSum(int a, int b, int expected)
        {
            var calculator = new Calculator();
            var result = calculator.Add(a, b);

            Assert.Equal(expected, result);
        }
    }
}
```

### Mocking (Moq)
```csharp
using Moq;
using Xunit;

namespace MyApp.Tests.Services
{
    public class UserServiceTests
    {
        [Fact]
        public void GetUserById_ValidId_ReturnsUser()
        {
            var mockRepo = new Mock<IUserRepository>();
            mockRepo.Setup(r => r.FindById(1))
                   .Returns(new User { Id = 1, Name = "John" });

            var service = new UserService(mockRepo.Object);
            var user = service.GetUserById(1);

            Assert.Equal("John", user.Name);
            mockRepo.Verify(r => r.FindById(1), Times.Once);
        }
    }
}
```

### Async Tests
```csharp
using System.Threading.Tasks;
using Xunit;

namespace MyApp.Tests.Services
{
    public class ApiServiceTests
    {
        [Fact]
        public async Task GetDataAsync_ReturnsData()
        {
            var service = new ApiService();
            var result = await service.GetDataAsync();

            Assert.NotNull(result);
            Assert.NotEmpty(result.Items);
        }
    }
}
```

### Exception Testing
```csharp
using System;
using Xunit;

namespace MyApp.Tests.Services
{
    public class ParserTests
    {
        [Fact]
        public void Parse_InvalidInput_ThrowsException()
        {
            var parser = new Parser();

            var exception = Assert.Throws<FormatException>(() => parser.Parse("invalid"));

            Assert.Equal("Invalid format", exception.Message);
        }
    }
}
```
