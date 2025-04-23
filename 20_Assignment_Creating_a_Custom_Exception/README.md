# Understanding Custom Exceptions in Python - Beginner's Guide

## What are Custom Exceptions?

Custom exceptions are user-defined exception classes that make your error handling more specific and meaningful to your application's domain.

## Baby Steps Explanation

### Step 1: Creating the Custom Exception Class
```python
class InvalidAgeError(Exception):  # Inherits from base Exception class
    """Raised when age is below minimum required"""
    pass  # Simple version - can add more functionality later
```
- Creates a new exception type `InvalidAgeError`
- Inherits from Python's base `Exception` class
- Docstring explains when this exception is raised

### Step 2: Writing the Validation Function
```python
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is invalid. Minimum age is 18.")
    print(f"Age {age} is valid. Proceeding...")
```
- Function checks if age meets minimum requirement
- Raises our custom exception with descriptive message if not
- Continues normally if age is valid

### Step 3: Handling the Exception
```python
try:
    check_age(16)  # This will raise our exception
    check_age(25)  # This line won't execute if exception occurs
except InvalidAgeError as e:
    print(f"Error: {e}")
    # Could add recovery code here
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("All checks passed successfully")
finally:
    print("Age verification complete")
```

## Key Features of Custom Exceptions

1. **Specific Error Handling**: Catch exactly the errors you expect
2. **Better Debugging**: More descriptive error messages
3. **Domain-Specific**: Match your application's terminology
4. **Hierarchy**: Can create exception inheritance trees

## Visual Representation

```
Exception Hierarchy
┌───────────────────────┐
│      Exception        │ ← Python base exception
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    InvalidAgeError    │ ← Our custom exception
└───────────────────────┘
```

## Common Mistakes

❌ Forgetting to inherit from `Exception`:
```python
class InvalidAgeError:  # Won't work as proper exception
    pass
```

❌ Raising without message:
```python
raise InvalidAgeError  # Less helpful than with message
```

## Practice Exercise

Create a `NegativeSalaryError` and validate salary:

```python
class NegativeSalaryError(Exception):
    pass

def validate_salary(salary):
    if salary < 0:
        raise NegativeSalaryError(f"Salary {salary} cannot be negative")
    print(f"Salary {salary} is valid")

try:
    validate_salary(-50000)
except NegativeSalaryError as e:
    print(f"Caught error: {e}")
```

## When to Use Custom Exceptions

1. When built-in exceptions don't precisely describe the error
2. For domain-specific error conditions
3. When you need to attach custom data to exceptions
4. To create exception hierarchies for complex systems
5. When you want consistent error handling across modules

## Advanced Usage

### Exception with Custom Attributes
```python
class InvalidAgeError(Exception):
    def __init__(self, age, min_age=18):
        self.age = age
        self.min_age = min_age
        super().__init__(f"Age {age} is below minimum {min_age}")

try:
    raise InvalidAgeError(16)
except InvalidAgeError as e:
    print(f"Received age: {e.age}, Required: {e.min_age}")
```

### Exception Chaining
```python
try:
    check_age(-5)  # Might raise ValueError first
except InvalidAgeError as e:
    raise InvalidAgeError("Invalid data") from e
```

## Final Notes

- Always inherit from `Exception` (or its subclasses)
- Include descriptive error messages
- Use for domain-specific error conditions
- Can add custom attributes and methods
- Follow Python's exception naming convention (ends with "Error")
- Document when your exceptions are raised

Understanding custom exceptions helps you write more robust and maintainable Python code by providing precise error handling tailored to your application's needs.