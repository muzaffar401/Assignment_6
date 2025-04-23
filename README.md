# Object-Oriented Programming (OOP) in Python - Complete Guide

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [Pillars of OOP](#pillars-of-oop)
3. [OOP Structure Diagram](#oop-structure-diagram)
4. [Python OOP Concepts with Assignments](#python-oop-concepts-with-assignments)
5. [Advanced OOP Topics](#advanced-oop-topics)

## Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather than functions and logic. In Python, everything is an object, making OOP a natural fit.

Key benefits of OOP:
- Modularity for easier maintenance
- Reusability through inheritance
- Flexibility via polymorphism
- Effective problem solving through abstraction

## Pillars of OOP

### 1. Encapsulation
Bundling data (attributes) and methods (functions) that operate on the data into a single unit (class), while restricting access to some components.

### 2. Abstraction
Hiding complex implementation details and showing only essential features of an object.

### 3. Inheritance
Creating new classes (child classes) from existing ones (parent classes) to reuse code.

### 4. Polymorphism
Ability of different objects to respond to the same method call in different ways.

## OOP Structure Diagram

```
┌───────────────────────┐
│      Class            │
├───────────────────────┤
│ - Class variables     │
│ - Instance variables  │
├───────────────────────┤
│ + __init__()          │
│ + Instance methods    │
│ @classmethod          │
│ @staticmethod         │
│ @property             │
└───────────┬───────────┘
            │
            │ Inheritance
            ▼
┌───────────────────────┐
│      Object           │
├───────────────────────┤
│ - State (attributes)  │
│ - Behavior (methods)  │
└───────────────────────┘
```

## Python OOP Concepts with Assignments

### 1. Using `self`

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

# Usage
s1 = Student("Alice", 95)
s1.display()
```

### 2. Using `cls`

```python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# Usage
c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # Output: 2
```

### 3. Public Variables and Methods

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting")

# Usage
my_car = Car("Toyota")
print(my_car.brand)  # Access public variable
my_car.start()       # Call public method
```

### 4. Class Variables and Class Methods

```python
class Bank:
    bank_name = "Global Bank"
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

# Usage
b1 = Bank()
b2 = Bank()
print(b1.bank_name)  # Output: Global Bank

Bank.change_bank_name("International Bank")
print(b2.bank_name)  # Output: International Bank
```

### 5. Static Variables and Static Methods

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Usage
print(MathUtils.add(5, 3))  # Output: 8
```

### 6. Constructors and Destructors

```python
class Logger:
    def __init__(self):
        print("Logger object created")
    
    def __del__(self):
        print("Logger object destroyed")

# Usage
logger = Logger()
del logger
```

### 7. Access Modifiers

```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private

# Usage
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)      # Works
print(emp._salary)   # Works but convention says "don't access directly"
# print(emp.__ssn)   # Error: AttributeError
```

### 8. The `super()` Function

```python
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Usage
teacher = Teacher("Mr. Smith", "Math")
print(teacher.name, teacher.subject)
```

### 9. Abstract Classes and Methods

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Usage
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
```

### 10. Instance Methods

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Usage
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
```

### 11. Class Methods

```python
class Book:
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Usage
b1 = Book("Python 101")
b2 = Book("OOP Principles")
print(Book.total_books)  # Output: 2
```

### 12. Static Methods

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Usage
print(TemperatureConverter.celsius_to_fahrenheit(30))  # Output: 86.0
```

### 13. Composition

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()

# Usage
car = Car()
car.start()  # Output: Engine started
```

### 14. Aggregation

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees else []
    
    def add_employee(self, employee):
        self.employees.append(employee)

# Usage
emp1 = Employee("John")
emp2 = Employee("Jane")
dept = Department("IT", [emp1])
dept.add_employee(emp2)
```

### 15. Method Resolution Order (MRO)

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Usage
d = D()
d.show()  # Output: B (due to MRO)
print(D.mro())  # Shows method resolution order
```

### 16. Function Decorators

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Usage
say_hello()
```

### 17. Class Decorators

```python
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

# Usage
p = Person()
print(p.greet())  # Output: Hello from Decorator!
```

### 18. Property Decorators

```python
class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Usage
p = Product(100)
print(p.price)  # Get
p.price = 150   # Set
del p.price     # Delete
```

### 19. `callable()` and `__call__()`

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Usage
double = Multiplier(2)
print(callable(double))  # Output: True
print(double(5))         # Output: 10
```

### 20. Custom Exception

```python
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return True

# Usage
try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")
```

### 21. Custom Iterable Class

```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Usage
for num in Countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1
```

## Advanced OOP Topics

### Magic Methods
Special methods with double underscores (__) that Python calls automatically in certain situations.

Common magic methods:
- `__str__`: String representation
- `__len__`: Length of object
- `__add__`: Addition operation
- `__eq__`: Equality comparison

### Multiple Inheritance
Python supports inheriting from multiple parent classes, but this can lead to the "diamond problem" which is resolved using MRO.

### Mixins
Small classes that are meant to provide optional features to other classes through multiple inheritance.

### Data Classes (Python 3.7+)
A decorator that automatically adds special methods like `__init__()` and `__repr__()` to classes.

### Slots
Optimization technique to explicitly declare data members and prevent creation of `__dict__`.

This comprehensive guide covers all fundamental and advanced OOP concepts in Python with practical examples. Each assignment demonstrates a specific OOP principle, making it easier to understand how object-oriented programming works in Python.