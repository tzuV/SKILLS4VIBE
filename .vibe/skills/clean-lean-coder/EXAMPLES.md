# Clean & Lean Coder - Examples

## Table of Contents
1. [Code Refactoring Examples](#1-code-refactoring-examples)
2. [Boilerplate Generation Examples](#2-boilerplate-generation-examples)
3. [Code Review Examples](#3-code-review-examples)
4. [Best Practice Examples](#4-best-practice-examples)

---

## 1. Code Refactoring Examples

### Example 1.1: Long Function → Single Responsibility

**Before (Violates Single Responsibility):**
```python
# app.py
def process_user_order(user_id, items):
    # Validate user
    if not user_id:
        raise ValueError("User ID is required")
    user = get_user_from_db(user_id)
    if not user:
        raise ValueError("User not found")
    if not user.is_active:
        raise ValueError("User is not active")
    
    # Validate items
    if not items:
        raise ValueError("Items are required")
    for item in items:
        if item.quantity <= 0:
            raise ValueError(f"Invalid quantity for {item.name}")
        if not item.product_id:
            raise ValueError(f"Product ID missing for {item.name}")
    
    # Calculate total
    subtotal = sum(item.price * item.quantity for item in items)
    tax = subtotal * 0.08
    total = subtotal + tax
    
    # Process payment
    if user.payment_method == "credit_card":
        charge = charge_credit_card(user.card_token, total)
    elif user.payment_method == "paypal":
        charge = process_paypal_payment(user.paypal_email, total)
    else:
        raise ValueError("Unsupported payment method")
    
    # Create order
    order = Order.objects.create(
        user=user,
        items=items,
        total=total,
        payment_charge_id=charge.id
    )
    
    # Send confirmation
    send_email(
        to=user.email,
        subject="Order Confirmation",
        body=f"Your order #{order.id} for ${total:.2f} has been placed."
    )
    
    return order
```

**After (Refactored):**
```python
# src/services/order_service.py
from src.validators import validate_user, validate_items
from src.payment import process_payment
from src.notifications import send_order_confirmation

class OrderService:
    def __init__(self, user_repo, payment_gateway, email_service):
        self.user_repo = user_repo
        self.payment_gateway = payment_gateway
        self.email_service = email_service
    
    def process_order(self, user_id, items):
        user = validate_user(self.user_repo, user_id)
        validate_items(items)
        
        total = self._calculate_total(items)
        charge = process_payment(self.payment_gateway, user, total)
        
        order = self._create_order(user, items, total, charge)
        self.email_service.send_order_confirmation(user, order)
        
        return order
    
    def _calculate_total(self, items):
        subtotal = sum(item.price * item.quantity for item in items)
        tax = subtotal * 0.08
        return subtotal + tax
    
    def _create_order(self, user, items, total, charge):
        return Order.objects.create(
            user=user,
            items=items,
            total=total,
            payment_charge_id=charge.id
        )

# src/validators.py
def validate_user(user_repo, user_id):
    """Validate user exists and is active."""
    if not user_id:
        raise ValueError("User ID is required")
    user = user_repo.get_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    if not user.is_active:
        raise ValueError("User is not active")
    return user

def validate_items(items):
    """Validate all items have valid data."""
    if not items:
        raise ValueError("Items are required")
    for item in items:
        if item.quantity <= 0:
            raise ValueError(f"Invalid quantity for {item.name}")
        if not item.product_id:
            raise ValueError(f"Product ID missing for {item.name}")

# src/payment.py
def process_payment(gateway, user, amount):
    """Process payment based on user's payment method."""
    if user.payment_method == "credit_card":
        return gateway.charge_credit_card(user.card_token, amount)
    elif user.payment_method == "paypal":
        return gateway.process_paypal(user.paypal_email, amount)
    else:
        raise ValueError("Unsupported payment method")

# src/notifications.py
def send_order_confirmation(user, order):
    """Send order confirmation email."""
    send_email(
        to=user.email,
        subject="Order Confirmation",
        body=f"Your order #{order.id} for ${order.total:.2f} has been placed."
    )
```

**Key Improvements:**
- ✅ Single Responsibility: Each function does one thing
- ✅ Dependency Injection: Services are injected, not hardcoded
- ✅ Better testability: Small, focused functions
- ✅ Better maintainability: Clear separation of concerns

---

### Example 1.2: Magic Numbers → Named Constants

**Before:**
```python
# app.py
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_eligible_for_scholarship(gpa):
    return gpa >= 3.5

def get_discount(customer_tier):
    if customer_tier == 1:
        return 0.10  # 10% discount
    elif customer_tier == 2:
        return 0.15  # 15% discount
    else:
        return 0.05  # 5% discount
```

**After:**
```python
# config/constants.py
# Grade thresholds
GRADE_A_THRESHOLD = 90
GRADE_B_THRESHOLD = 80
GRADE_C_THRESHOLD = 70
GRADE_D_THRESHOLD = 60

# Scholarship
SCHOLARSHIP_GPA_THRESHOLD = 3.5

# Customer discounts
CUSTOMER_TIER_1_DISCOUNT = 0.10
CUSTOMER_TIER_2_DISCOUNT = 0.15
CUSTOMER_DEFAULT_DISCOUNT = 0.05

# app.py
from config.constants import (
    GRADE_A_THRESHOLD, GRADE_B_THRESHOLD, GRADE_C_THRESHOLD,
    GRADE_D_THRESHOLD, SCHOLARSHIP_GPA_THRESHOLD,
    CUSTOMER_TIER_1_DISCOUNT, CUSTOMER_TIER_2_DISCOUNT,
    CUSTOMER_DEFAULT_DISCOUNT
)

def calculate_grade(score):
    if score >= GRADE_A_THRESHOLD:
        return "A"
    elif score >= GRADE_B_THRESHOLD:
        return "B"
    elif score >= GRADE_C_THRESHOLD:
        return "C"
    elif score >= GRADE_D_THRESHOLD:
        return "D"
    else:
        return "F"

def is_eligible_for_scholarship(gpa):
    return gpa >= SCHOLARSHIP_GPA_THRESHOLD

def get_discount(customer_tier):
    if customer_tier == 1:
        return CUSTOMER_TIER_1_DISCOUNT
    elif customer_tier == 2:
        return CUSTOMER_TIER_2_DISCOUNT
    else:
        return CUSTOMER_DEFAULT_DISCOUNT
```

**Key Improvements:**
- ✅ Magic numbers replaced with descriptive names
- ✅ Constants centralized in `config/`
- ✅ Easy to update thresholds without touching logic
- ✅ Better maintainability

---

### Example 1.3: Nested Conditionals → Guard Clauses

**Before:**
```python
# app.py
def process_data(data):
    if data:
        if data.is_valid:
            if data.type == "user":
                result = process_user_data(data)
            elif data.type == "order":
                result = process_order_data(data)
            else:
                result = None
        else:
            result = None
    else:
        result = None
    
    return result
```

**After:**
```python
# app.py
def process_data(data):
    if not data:
        return None
    
    if not data.is_valid:
        return None
    
    if data.type == "user":
        return process_user_data(data)
    elif data.type == "order":
        return process_order_data(data)
    
    return None
```

**Key Improvements:**
- ✅ Reduced nesting depth (flat is better)
- ✅ Early returns for error cases
- ✅ More readable control flow
- ✅ Same logic, better structure

---

### Example 1.4: Repeated Logic → utils/

**Before:**
```python
# controllers/user_controller.py
def create_user(request):
    email = request.json.get('email')
    if not email or '@' not in email:
        return {"error": "Invalid email"}, 400
    # ... rest of controller

# controllers/order_controller.py
def create_order(request):
    email = request.json.get('email')
    if not email or '@' not in email:
        return {"error": "Invalid email"}, 400
    # ... rest of controller

# services/notification_service.py
def send_notification(email, message):
    if not email or '@' not in email:
        raise ValueError("Invalid email")
    # ... rest of service
```

**After:**
```python
# utils/validators.py
import re

def validate_email(email):
    """Validate email format."""
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# controllers/user_controller.py
from utils.validators import validate_email

def create_user(request):
    email = request.json.get('email')
    if not validate_email(email):
        return {"error": "Invalid email"}, 400
    # ... rest of controller

# controllers/order_controller.py
from utils.validators import validate_email

def create_order(request):
    email = request.json.get('email')
    if not validate_email(email):
        return {"error": "Invalid email"}, 400
    # ... rest of controller

# services/notification_service.py
from utils.validators import validate_email

def send_notification(email, message):
    if not validate_email(email):
        raise ValueError("Invalid email")
    # ... rest of service
```

**Key Improvements:**
- ✅ DRY: Email validation logic in one place
- ✅ Better validation (regex instead of simple check)
- ✅ Easy to update validation for all uses
- ✅ Consistent error handling

---

## 2. Boilerplate Generation Examples

### Example 2.1: Creating utils/ Structure

**Trigger**: "Create a utils directory for my Python project"

**Generated Output:**
```bash
# Created directory structure
utils/
├── __init__.py
├── helpers.py
├── validators.py
├── formatters.py
└── exceptions.py
```

**Generated Files:**

`utils/__init__.py`:
```python
"""Utility functions for the project."""

from .helpers import (
    chunk_list,
    flatten_list,
    get_first,
    get_last,
)
from .validators import (
    validate_email,
    validate_phone,
    validate_required,
)
from .formatters import (
    format_currency,
    format_date,
    format_percentage,
)
from .exceptions import (
    ValidationError,
    ConfigurationError,
)

__all__ = [
    # Helpers
    'chunk_list', 'flatten_list', 'get_first', 'get_last',
    # Validators
    'validate_email', 'validate_phone', 'validate_required',
    # Formatters
    'format_currency', 'format_date', 'format_percentage',
    # Exceptions
    'ValidationError', 'ConfigurationError',
]
```

`utils/helpers.py`:
```python
"""General helper functions."""

from typing import Any, Iterable, List, Optional, TypeVar

T = TypeVar('T')

def chunk_list(items: List[T], size: int) -> List[List[T]]:
    """Split a list into chunks of specified size."""
    return [items[i:i + size] for i in range(0, len(items), size)]

def flatten_list(nested: Iterable[Iterable[T]]) -> List[T]:
    """Flatten a nested list."""
    return [item for sublist in nested for item in sublist]

def get_first(items: List[T], default: Optional[T] = None) -> Optional[T]:
    """Get first item from list or return default."""
    return items[0] if items else default

def get_last(items: List[T], default: Optional[T] = None) -> Optional[T]:
    """Get last item from list or return default."""
    return items[-1] if items else default
```

---

### Example 2.2: Creating config/ Structure

**Trigger**: "Create a config directory for my project"

**Generated Output:**
```bash
# Created directory structure
config/
├── __init__.py
├── settings.py
├── constants.py
└── .env.example
```

`config/settings.py`:
```python
"""Application settings loaded from environment variables."""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings."""
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Database
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "myapp")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    
    # API
    API_KEY: Optional[str] = os.getenv("API_KEY")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://api.example.com")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "30"))
    
    # Application
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
```

`config/constants.py`:
```python
"""Application constants."""

# HTTP Status Codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_ERROR = 500

# Pagination
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Date Formats
DATE_FORMAT_ISO = "%Y-%m-%d"
DATE_FORMAT_HUMAN = "%B %d, %Y"
DATETIME_FORMAT_ISO = "%Y-%m-%dT%H:%M:%S"
DATETIME_FORMAT_HUMAN = "%B %d, %Y at %I:%M %p"

# Validation
MIN_PASSWORD_LENGTH = 8
MAX_USERNAME_LENGTH = 50
MAX_EMAIL_LENGTH = 255

# Retry Logic
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 1
RETRY_BACKOFF_MULTIPLIER = 2
```

`.env.example`:
```bash
# Environment
ENVIRONMENT=development
DEBUG=True

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
DB_USER=postgres
DB_PASSWORD=

# API
API_KEY=
API_BASE_URL=https://api.example.com
API_TIMEOUT=30

# Application
SECRET_KEY=change-me-in-production
ALLOWED_ORIGINS=*

# Logging
LOG_LEVEL=INFO
```

---

### Example 2.3: Unit Test Stub Generation

**Trigger**: "Generate unit tests for utils/helpers.py"

**Generated Output:**
```python
# tests/unit/test_helpers.py
"""Unit tests for utils/helpers.py"""

import pytest
from utils.helpers import (
    chunk_list,
    flatten_list,
    get_first,
    get_last,
)


class TestChunkList:
    """Tests for chunk_list function."""
    
    def test_empty_list(self):
        """Empty list returns empty list."""
        assert chunk_list([], 2) == []
    
    def test_single_chunk(self):
        """List smaller than chunk size returns single chunk."""
        assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]
    
    def test_exact_multiple(self):
        """List exactly divisible by chunk size."""
        assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    
    def test_uneven_division(self):
        """List not evenly divisible by chunk size."""
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    
    def test_size_one(self):
        """Chunk size of 1."""
        assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]


class TestFlattenList:
    """Tests for flatten_list function."""
    
    def test_empty_list(self):
        """Empty nested list returns empty list."""
        assert flatten_list([]) == []
    
    def test_single_level(self):
        """Single level list."""
        assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    
    def test_deeply_nested(self):
        """Deeply nested list."""
        assert flatten_list([[1, [2, [3]]], [4]]) == [1, 2, 3, 4]


class TestGetFirst:
    """Tests for get_first function."""
    
    def test_non_empty_list(self):
        """Returns first element of non-empty list."""
        assert get_first([1, 2, 3]) == 1
    
    def test_empty_list_with_default(self):
        """Returns default for empty list."""
        assert get_first([], "default") == "default"
    
    def test_empty_list_no_default(self):
        """Returns None for empty list with no default."""
        assert get_first([]) is None


class TestGetLast:
    """Tests for get_last function."""
    
    def test_non_empty_list(self):
        """Returns last element of non-empty list."""
        assert get_last([1, 2, 3]) == 3
    
    def test_empty_list_with_default(self):
        """Returns default for empty list."""
        assert get_last([], "default") == "default"
    
    def test_empty_list_no_default(self):
        """Returns None for empty list with no default."""
        assert get_last([]) is None
```

---

## 3. Code Review Examples

### Example 3.1: Real-Time Code Review

**User Code:**
```python
# app.py
def calculate_totals(data):
    x = 0
    for i in range(len(data)):
        if data[i].is_valid:
            x += data[i].amount * 1.08
    return x
```

**Skill Response:**

```
⚠️ **Code Review Findings for app.py:calculate_totals**

### Issues Found:

1. **❌ Magic Number (Line 4)**
   - **Problem**: Hardcoded `1.08` (tax rate)
   - **Impact**: Difficult to maintain; tax rate changes require code changes
   - **Fix**: Move to `config/constants.py`
   
   ```python
   # config/constants.py
   TAX_RATE = 1.08
   
   # app.py
   from config.constants import TAX_RATE
   
   def calculate_totals(data):
       total = 0
       for item in data:
           if item.is_valid:
               total += item.amount * TAX_RATE
       return total
   ```

2. **❌ Variable Naming (Line 2)**
   - **Problem**: `x` is not intention-revealing
   - **Impact**: Hard to understand what the variable represents
   - **Fix**: Rename to `total`

3. **❌ Loop Variable (Line 3)**
   - **Problem**: Using `i` index when you only need the item
   - **Impact**: Less Pythonic, harder to read
   - **Fix**: Iterate directly over items

4. **❌ Function Name (Line 1)**
   - **Problem**: `calculate_totals` doesn't specify what type of totals
   - **Fix**: Rename to `calculate_valid_items_total` or similar

### Improved Version:

```python
# app.py
from config.constants import TAX_RATE

def calculate_valid_items_total(items):
    """Calculate total amount for valid items including tax."""
    total = 0
    for item in items:
        if item.is_valid:
            total += item.amount * TAX_RATE
    return total
```

✅ **All issues resolved!**
```

---

### Example 3.2: System Prompt Rule Violation

**User Code:**
```python
# main.py
import requests

def get_weather(city):
    api_key = "sk-12345"  # Hardcoded API key
    url = f"https://api.weather.com/v1?city={city}&key={api_key}"
    response = requests.get(url)
    return response.json()
```

**Skill Response:**

```
❌ **CRITICAL: System Prompt Rule Violation**

### Violation Details:
- **Rule**: "Never hardcode secrets, API keys, or credentials"
- **Location**: main.py:3
- **Severity**: HIGH

### Fix Required:

1. **Move API key to environment variable:**
   ```bash
   # .env
   WEATHER_API_KEY=sk-12345
   ```

2. **Update code:**
   ```python
   # config/settings.py
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   class Settings:
       WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
   
   settings = Settings()
   
   # main.py
   from config.settings import settings
   import requests
   
   def get_weather(city):
       url = f"https://api.weather.com/v1?city={city}&key={settings.WEATHER_API_KEY}"
       response = requests.get(url)
       return response.json()
   ```

3. **Add .env to .gitignore:**
   ```bash
   echo ".env" >> .gitignore
   ```

⚠️ **Do not commit until this is fixed!**
```

---

## 4. Best Practice Examples

### Example 4.1: Custom Exceptions

**Before:**
```python
# app.py
def process_user(user):
    if not user:
        raise ValueError("User is required")
    if not user.email:
        raise ValueError("Email is required")
    if not user.is_active:
        raise ValueError("User is not active")
    # ... processing
```

**After:**
```python
# src/exceptions.py
class UserValidationError(ValueError):
    """Base exception for user validation errors."""
    pass

class UserNotFoundError(UserValidationError):
    """Raised when user is None."""
    pass

class EmailMissingError(UserValidationError):
    """Raised when user email is missing."""
    pass

class UserInactiveError(UserValidationError):
    """Raised when user is not active."""
    pass

# app.py
from src.exceptions import (
    UserNotFoundError,
    EmailMissingError,
    UserInactiveError,
)

def process_user(user):
    if not user:
        raise UserNotFoundError("User is required")
    if not user.email:
        raise EmailMissingError("Email is required")
    if not user.is_active:
        raise UserInactiveError("User is not active")
    # ... processing
```

**Benefits:**
- ✅ More specific error handling
- ✅ Easier to catch specific exceptions
- ✅ Better error messages and debugging
- ✅ Domain-specific error hierarchy

---

### Example 4.2: Dependency Injection

**Before (Tightly Coupled):**
```python
# services/user_service.py
class UserService:
    def __init__(self):
        self.db = DatabaseConnection()  # Hardcoded dependency
    
    def get_user(self, user_id):
        return self.db.query("SELECT * FROM users WHERE id = %s", user_id)

# tests/test_user_service.py
def test_get_user():
    service = UserService()  # Can't mock the database!
    user = service.get_user(1)
    assert user.id == 1
```

**After (Dependency Injected):**
```python
# services/user_service.py
class UserService:
    def __init__(self, db_connection):  # Dependency injected
        self.db = db_connection
    
    def get_user(self, user_id):
        return self.db.query("SELECT * FROM users WHERE id = %s", user_id)

# main.py
from database import DatabaseConnection
from services.user_service import UserService

# Real usage
db = DatabaseConnection()
service = UserService(db)

# tests/test_user_service.py
from unittest.mock import Mock
from services.user_service import UserService

def test_get_user():
    # Mock the database
    mock_db = Mock()
    mock_db.query.return_value = Mock(id=1, name="Test User")
    
    service = UserService(mock_db)
    user = service.get_user(1)
    
    assert user.id == 1
    mock_db.query.assert_called_once_with(
        "SELECT * FROM users WHERE id = %s", 1
    )
```

**Benefits:**
- ✅ Easy to test (dependencies can be mocked)
- ✅ Easy to swap implementations
- ✅ Loose coupling between components
- ✅ Better adherence to Dependency Inversion Principle

---

### Example 4.3: Using Built-ins and Comprehensions

**Before:**
```python
# app.py
def get_valid_emails(users):
    result = []
    for user in users:
        if user.is_active and user.email:
            result.append(user.email)
    return result

def double_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

def get_user_names(users):
    result = []
    for user in users:
        result.append(user.name)
    return result
```

**After:**
```python
# app.py
def get_valid_emails(users):
    """Get emails of all active users."""
    return [user.email for user in users if user.is_active and user.email]

def double_numbers(numbers):
    """Double all numbers in list."""
    return [num * 2 for num in numbers]

def get_user_names(users):
    """Get names of all users."""
    return [user.name for user in users]

# Or using map for simple transformations
def double_numbers(numbers):
    """Double all numbers in list."""
    return list(map(lambda x: x * 2, numbers))

def get_user_names(users):
    """Get names of all users."""
    return list(map(lambda user: user.name, users))
```

**Benefits:**
- ✅ More concise and readable
- ✅ Pythonic idioms
- ✅ Often faster (list comprehensions are optimized)
- ✅ Easier to understand intent

---

## Summary

These examples demonstrate the **Clean & Lean Coder** skill in action:

1. **Refactoring**: Breaking down monolithic code into maintainable pieces
2. **Boilerplate Generation**: Creating standard structures and files
3. **Code Review**: Identifying violations and suggesting improvements
4. **Best Practices**: Applying SOLID, DRY, KISS, and other principles

Each example shows **before/after** comparisons with clear explanations of the improvements.
