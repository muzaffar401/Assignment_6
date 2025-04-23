# Understanding Constructors and Destructors in Python - Beginner's Guide

## What are Constructors and Destructors?

Constructors and destructors are special methods that automatically run when objects are created and destroyed.

### Constructor (`__init__`)
- Runs when object is created
- Used for initialization
- Takes `self` parameter

### Destructor (`__del__`)
- Runs when object is about to be destroyed
- Used for cleanup
- Takes `self` parameter

## Baby Steps Explanation

### Step 1: Basic Class Structure
```python
class Logger:
    pass
```
This creates an empty class.

### Step 2: Adding Constructor
```python
class Logger:
    def __init__(self):
        print("Logger object created")
```
- `__init__` is called automatically
- Prints message when object is created

### Step 3: Adding Destructor
```python
class Logger:
    def __init__(self):
        print("Logger object created")
        
    def __del__(self):
        print("Logger object destroyed")
```
- `__del__` is called when object is deleted
- Prints message when object is destroyed

### Step 4: Using the Class
```python
# Create object (constructor runs)
logger = Logger()

# Delete object (destructor runs)
del logger
```

## Key Points

1. **Constructor** (`__init__`):
   - First method called when creating object
   - Typically used to set initial values
   - Can take parameters

2. **Destructor** (`__del__`):
   - Called when object is garbage collected
   - Not guaranteed to run at specific time
   - Used for cleanup operations

## Visual Representation

```
Object Lifecycle:
Create → [__init__] → Use → [__del__] → Destroy
```

## Common Mistakes

❌ Forgetting `self` parameter:
```python
def __init__():  # Missing self
    print("Created")
```

❌ Relying too much on `__del__`:
- Python's garbage collection is non-deterministic
- Don't use for critical cleanup (use context managers instead)

## Practice Exercise

Create a `FileHandler` class that:
1. Prints "Opening file" when created
2. Prints "Closing file" when destroyed
3. Has a method to read file content

```python
class FileHandler:
    def __init__(self, filename):
        print(f"Opening file {filename}")
        self.filename = filename
    
    def read(self):
        with open(self.filename) as f:
            return f.read()
    
    def __del__(self):
        print(f"Closing file {self.filename}")

# Test it
handler = FileHandler("example.txt")
print(handler.read())
del handler
```

## When to Use

- **Constructors**:
  - Setting default values
  - Validating inputs
  - Opening resources

- **Destructors**:
  - Closing files
  - Releasing resources
  - Logging object destruction

## Important Notes

1. Destructors are not reliable for critical cleanup
2. Use context managers (`with` statement) for resource management
3. Constructors can return `None` only (cannot return values)

## Final Example with Parameters

```python
class Student:
    def __init__(self, name):
        print(f"Creating student: {name}")
        self.name = name
    
    def __del__(self):
        print(f"Deleting student: {self.name}")

# Usage
s1 = Student("Alice")
s2 = Student("Bob")
del s1
```

Understanding constructors and destructors helps you manage object lifecycle in Python programs effectively.