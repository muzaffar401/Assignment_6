# Understanding Access Modifiers in Python - Beginner's Guide

## What are Access Modifiers?

Access modifiers control the visibility and accessibility of class members (variables and methods). Python has three levels of access control:

1. **Public**: No restrictions (default)
2. **Protected**: Conventionally marked with single underscore `_`
3. **Private**: Marked with double underscore `__`

## Baby Steps Explanation

### Step 1: Creating Class with Different Access Levels
```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name      # Public
        self._salary = salary  # Protected
        self.__ssn = ssn      # Private
```

### Step 2: Accessing Public Member
```python
emp = Employee("Ali", 50000, "123-45-6789")
print(emp.name)  # Works fine - public access
```

### Step 3: Accessing Protected Member
```python
print(emp._salary)  # Works but convention says "don't do this directly"
```

### Step 4: Trying to Access Private Member
```python
# print(emp.__ssn)  # Will cause AttributeError
```

### Step 5: Accessing Private Member via Name Mangling
```python
print(emp._Employee__ssn)  # Works but should be avoided
```

### Step 6: Proper Way to Access Private Data
```python
class Employee:
    # ... (previous code)
    
    def get_ssn(self):  # Public method to access private data
        return self.__ssn

print(emp.get_ssn())  # Proper way to access private data
```

## Key Differences

| Access Type | Prefix   | Accessibility                     | Convention |
|-------------|---------|-----------------------------------|------------|
| Public      | None    | Anywhere                          | No restrictions |
| Protected   | `_`     | Class and subclasses              | "Don't touch from outside" |
| Private     | `__`    | Only within class                 | "Really don't touch" |

## Visual Representation

```
Employee Object
┌───────────────────────┐
│ Public:               │
│   name                │ ← Anyone can access
│                       │
│ Protected:            │
│   _salary             │ ← Should only be accessed by class/subclasses
│                       │
│ Private:              │
│   __ssn (name mangled)│ ← Only accessible within class
└───────────────────────┘
```

## Best Practices

1. **Public Members**:
   - For interface you want to expose
   - Safe for external use

2. **Protected Members**:
   - Use single underscore prefix `_`
   - Document that it's for internal use
   - Subclasses may access them

3. **Private Members**:
   - Use double underscore prefix `__`
   - Only access through public methods
   - Prevents accidental modification

## Common Mistakes

❌ Trying to access private members directly:
```python
print(emp.__ssn)  # Error!
```

❌ Forgetting Python's access control is by convention:
```python
emp._salary = -1000  # Works but violates encapsulation
```

## Practice Exercise

Create a `BankAccount` class with:
1. Public method `deposit()`
2. Protected attribute `_balance`
3. Private attribute `__pin`
4. Public method to check balance

```python
class BankAccount:
    def __init__(self, balance, pin):
        self._balance = balance
        self.__pin = pin
    
    def deposit(self, amount):
        self._balance += amount
    
    def check_balance(self, pin):
        if pin == self.__pin:
            return self._balance
        return "Invalid PIN"

# Test it
account = BankAccount(1000, "1234")
account.deposit(500)
print(account.check_balance("1234"))  # Should show 1500
print(account.check_balance("0000"))  # Should show "Invalid PIN"
```

## Final Notes

- Python doesn't enforce access restrictions - it's programmer's responsibility
- Use access modifiers to communicate intent
- Private members use name mangling (`_ClassName__member`)
- Prefer public methods to access protected/private data
- Follow conventions to make your code more maintainable

Understanding access modifiers helps you write more secure and maintainable object-oriented code in Python. While Python doesn't enforce these restrictions strictly, following these conventions makes your code's intent clearer to other developers.