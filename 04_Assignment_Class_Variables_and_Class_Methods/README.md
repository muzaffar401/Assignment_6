# Understanding Class Variables and Class Methods in Python - Beginner's Guide

## What are Class Variables and Class Methods?

Class variables are variables that are shared by all instances of a class. Class methods are methods that work with the class itself rather than individual instances.

## Baby Steps Explanation

### Step 1: Creating a Class with Class Variable
```python
class Bank:
    bank_name = "State Bank"  # This is a class variable
```
- `bank_name` is defined at the class level
- All instances will share this same variable

### Step 2: Adding a Class Method
```python
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
```
- `@classmethod` decorator marks this as a class method
- `cls` parameter refers to the class itself (like `self` refers to instance)
- We can modify class variables using `cls`

### Step 3: Creating Instances
```python
account1 = Bank()
account2 = Bank()
```
- Both instances will initially have the same `bank_name`

### Step 4: Using the Class Method
```python
Bank.change_bank_name("National Bank")
```
- Changes the `bank_name` for all instances
- Can also be called on an instance: `account1.change_bank_name(...)`

## Key Features

1. **Shared Data**: Class variables are shared across all instances
2. **Class-Level Operations**: Class methods operate on the class itself
3. **Persistent Changes**: Changing class variables affects all instances

## Visual Representation

```
Bank Class
┌───────────────────────┐
│ Class Variable:       │
│   bank_name           │
│                       │
│ Class Method:         │
│   - change_bank_name()│
└───────────┬───────────┘
            │
            ▼
Instances:  account1    account2
            (both share bank_name)
```

## Common Mistakes

❌ Confusing class and instance variables:
```python
def __init__(self):
    self.bank_name = "State Bank"  # This creates instance variables
```

❌ Forgetting `@classmethod` decorator:
```python
def change_bank_name(cls, name):  # Without decorator, won't work as class method
    cls.bank_name = name
```

## Practice Exercise

Create a `Company` class with:
1. Class variable `company_name`
2. Class method to change company name
3. Instance variable `employee_name`

```python
class Company:
    company_name = "Tech Corp"
    
    def __init__(self, employee_name):
        self.employee_name = employee_name
    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

# Test it
emp1 = Company("Alice")
emp2 = Company("Bob")

print(emp1.company_name)  # Output: Tech Corp
print(emp2.company_name)  # Output: Tech Corp

Company.change_company_name("Innovate Inc")

print(emp1.company_name)  # Output: Innovate Inc
print(emp2.company_name)  # Output: Innovate Inc
```

## When to Use Class Methods

1. When you need to work with class-level data
2. For factory methods that create instances
3. When the operation affects all instances
4. For alternative constructors

## Final Notes

- Class variables are shared across all instances
- Class methods use `@classmethod` decorator
- `cls` refers to the class in class methods
- Changes to class variables affect all instances
- Useful for maintaining shared state across objects

Understanding class variables and methods is essential for managing shared data and behavior across all instances of a class in Python.