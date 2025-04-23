# Understanding Method Resolution Order (MRO) in Python - Beginner's Guide

## What is Method Resolution Order (MRO)?

MRO is the order in which Python looks for methods in a class hierarchy, especially important in multiple inheritance scenarios (like diamond inheritance).

## Baby Steps Explanation

### Step 1: Creating the Base Class
```python
class A:
    def show(self):
        print("Show from class A")
```
- This is our base class with a `show()` method
- All other classes will inherit from this directly or indirectly

### Step 2: Creating Intermediate Classes
```python
class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")
```
- Both `B` and `C` inherit from `A`
- Both override the `show()` method with their own versions

### Step 3: Creating the Diamond Structure
```python
class D(B, C):  # Inherits from both B and C
    pass  # Doesn't implement its own show()
```
- This creates the "diamond" inheritance pattern:
  ```
      A
     / \
    B   C
     \ /
      D
```

### Step 4: Observing MRO in Action
```python
d = D()
d.show()  # Which show() will be called?
```
Output:
```
Show from class B
```

### Step 5: Viewing the MRO
```python
print(D.__mro__)
```
Output (shows the search order):
```
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

## Key Points About MRO

1. **Order Matters**: The inheritance order in class definition (`class D(B, C)`) determines MRO
2. **Depth-First, Left-to-Right**: Python searches:
   - Current class (D)
   - Then first parent (B)
   - Then B's parents (A)
   - Then second parent (C)
   - Then C's parents (A) - but A already visited
3. **C3 Linearization**: Python uses this algorithm to determine MRO

## Visual Representation of MRO

```
Method Lookup Order for D:
1. D
2. B (first in inheritance list)
3. C (second in inheritance list)
4. A (parent of both B and C)
5. object (base Python class)
```

## Common Mistakes

❌ Creating ambiguous inheritance:
```python
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass  # Error! Inconsistent hierarchy
```

❌ Assuming parent order doesn't matter:
```python
class D(C, B):  # Different from D(B, C)
    pass
d = D()
d.show()  # Now calls C's show() instead of B's
```

## Practice Exercise

Create a similar hierarchy with different method names to observe MRO:

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Hybrid(Dog, Cat):
    pass

pet = Hybrid()
pet.speak()  # Which speak() will be called?
print(Hybrid.__mro__)
```

## When MRO Matters

1. In multiple inheritance scenarios
2. When method names collide in parent classes
3. When you need to understand which method will be called
4. When designing complex class hierarchies

## Advanced Usage

### Calling Specific Parent's Method
```python
class D(B, C):
    def show(self):
        C.show(self)  # Explicitly call C's show()
        print("Additional stuff from D")
```

### super() with MRO
```python
class D(B, C):
    def show(self):
        super().show()  # Follows MRO to call B's show()
```

## Final Notes

- MRO ensures predictable method lookup in complex inheritance
- Use `class.__mro__` to inspect the method resolution order
- The order of base classes matters in multiple inheritance
- Python raises TypeError for inconsistent hierarchies
- MRO follows C3 linearization rules

Understanding MRO is crucial when working with multiple inheritance in Python, helping you predict and control which methods will be called in complex class hierarchies.