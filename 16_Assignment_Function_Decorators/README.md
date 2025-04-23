# Understanding Function Decorators in Python - Beginner's Guide

## What are Function Decorators?

Decorators are functions that modify the behavior of other functions without changing their core functionality. They wrap another function to extend its behavior.

## Baby Steps Explanation

### Step 1: Creating the Decorator Function
```python
def log_function_call(func):  # Takes a function as input
    def wrapper():  # Inner function that does the wrapping
        print("Function is being called")  # Added behavior
        func()  # Call the original function
    return wrapper  # Return the wrapped function
```
- `log_function_call` is our decorator
- It takes a function `func` as parameter
- Defines an inner `wrapper` function that:
  - Adds new behavior (print statement)
  - Calls the original function
- Returns the wrapper function

### Step 2: Applying the Decorator
```python
@log_function_call  # This is the decorator syntax
def say_hello():
    print("Hello, World!")
```
- The `@` symbol applies the decorator
- Equivalent to: `say_hello = log_function_call(say_hello)`

### Step 3: Calling the Decorated Function
```python
say_hello()
```
Output:
```
Function is being called
Hello, World!
```

## Key Features of Decorators

1. **Modify Behavior**: Add functionality before/after function calls
2. **Reusable**: Same decorator can be applied to multiple functions
3. **Non-Invasive**: Don't need to modify original function code
4. **Flexible**: Can work with functions that take arguments

## Visual Representation

```
Original Function        Decorated Function
┌─────────────────┐      ┌─────────────────┐
│ say_hello()     │      │ wrapper()       │
│ print("Hello")  │  →   │ print("Calling")│
└─────────────────┘      │ say_hello()     │
                         └─────────────────┘
```

## Common Mistakes

❌ Forgetting to call the original function:
```python
def bad_decorator(func):
    def wrapper():
        print("Oops, forgot to call func()")
    return wrapper
```

❌ Not returning the wrapper:
```python
def bad_decorator(func):
    def wrapper():
        func()
    # Forgot return wrapper!
```

## Practice Exercise

Create a decorator `timer` that prints how long a function takes to execute:

```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end-start:.2f} seconds")
    return wrapper

@timer
def long_operation():
    time.sleep(1)

long_operation()
```

## When to Use Decorators

1. Logging function calls
2. Timing function execution
3. Authentication/authorization checks
4. Input validation
5. Caching/memoization

## Advanced Usage

### Decorators with Arguments
```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```

### Preserving Function Metadata
```python
from functools import wraps

def decorator(func):
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Final Notes

- Decorators are powerful tools for modifying function behavior
- They follow the "Decorator Pattern" from software design
- Multiple decorators can be stacked (`@decor1 @decor2 def func()`)
- The `functools.wraps` decorator helps preserve metadata
- Used extensively in Python frameworks (Flask, Django etc.)

Understanding decorators helps you write more modular and maintainable Python code by separating cross-cutting concerns from core functionality.