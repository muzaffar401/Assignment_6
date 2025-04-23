# Understanding Class Decorators in Python - Beginner's Guide

## What are Class Decorators?

Class decorators are functions that modify or enhance classes, similar to how function decorators modify functions. They take a class as input and return a modified class.

## Baby Steps Explanation

### Step 1: Creating the Class Decorator
```python
def add_greeting(cls):  # Takes a class as input
    # Define the new method we want to add
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the method to the class
    cls.greet = greet
    
    # Return the modified class
    return cls
```
- `add_greeting` is our class decorator
- It takes a class `cls` as parameter
- Defines a new `greet()` method
- Adds this method to the class
- Returns the modified class

### Step 2: Applying the Decorator
```python
@add_greeting  # Apply the decorator to Person class
class Person:
    def __init__(self, name):
        self.name = name
```
- The `@` symbol applies the decorator
- Equivalent to: `Person = add_greeting(Person)`

### Step 3: Using the Decorated Class
```python
p = Person("Alice")
print(p.name)     # Original attribute
print(p.greet())  # New method added by decorator
```
Output:
```
Alice
Hello from Decorator!
```

## Key Features of Class Decorators

1. **Modify Classes**: Add/change methods and attributes
2. **Reusable**: Same decorator can modify multiple classes
3. **Non-Invasive**: Don't need to modify original class code
4. **Flexible**: Can add any number of methods/properties

## Visual Representation

```
Original Class            Decorated Class
┌─────────────────┐      ┌─────────────────┐
│ Person          │      │ Person          │
│ - name          │  →   │ - name          │
│                 │      │ + greet()       │
└─────────────────┘      └─────────────────┘
```

## Common Mistakes

❌ Forgetting to return the modified class:
```python
def bad_decorator(cls):
    cls.new_method = lambda self: "Hello"
    # Forgot to return cls!
```

❌ Modifying class in place without returning:
```python
def bad_decorator(cls):
    cls.new_method = lambda self: "Hello"
    return None  # Wrong return value
```

## Practice Exercise

Create a class decorator `add_timestamp` that adds a `created_at` attribute to classes:

```python
from datetime import datetime

def add_timestamp(cls):
    original_init = cls.__init__
    
    def __init__(self, *args, **kwargs):
        self.created_at = datetime.now()
        original_init(self, *args, **kwargs)
    
    cls.__init__ = __init__
    return cls

@add_timestamp
class Note:
    def __init__(self, text):
        self.text = text

note = Note("Remember decorators!")
print(note.text)
print(note.created_at)
```

## When to Use Class Decorators

1. Adding common functionality to multiple classes
2. Registering classes with a framework
3. Modifying class attributes/methods
4. Implementing class-level validation
5. Adding logging/monitoring capabilities

## Advanced Usage

### Decorator with Parameters
```python
def add_method(method_name, method):
    def decorator(cls):
        setattr(cls, method_name, method)
        return cls
    return decorator

@add_method("say_bye", lambda self: "Goodbye!")
class Person:
    pass

p = Person()
print(p.say_bye())  # Output: Goodbye!
```

### Multiple Decorators
```python
@decorator1
@decorator2
class MyClass:
    pass
```

## Final Notes

- Class decorators are powerful tools for modifying class behavior
- They follow similar principles to function decorators
- Can be used for metaprogramming and framework development
- Multiple decorators can be stacked on a single class
- Used extensively in Python frameworks (Django models, etc.)

Understanding class decorators helps you write more flexible and maintainable Python code by enabling dynamic class modification and extension.