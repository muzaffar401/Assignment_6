# Understanding Iterable Classes in Python - Beginner's Guide

## What are Iterable Classes?

Iterable classes are classes that can be used in `for` loops by implementing the iterator protocol (`__iter__` and `__next__` methods).

## Baby Steps Explanation

### Step 1: Creating the Countdown Class
```python
class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize starting number
```
- Constructor takes the starting number
- Stores it as an instance variable

### Step 2: Implementing `__iter__`
```python
    def __iter__(self):
        self.current = self.start  # Reset counter to start
        return self  # Returns the iterator object
```
- Initializes/resets the iteration state
- Must return an object with `__next__` method
- Here we return `self` since our class implements both methods

### Step 3: Implementing `__next__`
```python
    def __next__(self):
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration  # Signal iteration complete
```
- Returns next value in sequence
- Updates state for next call
- Raises `StopIteration` when done

### Step 4: Using the Iterable
```python
# Create countdown from 5 to 0
for num in Countdown(5):
    print(num)
```
Output:
```
5
4
3
2
1
0
```

## Key Features of Iterable Classes

1. **Works in for-loops**: Can be used directly in `for` statements
2. **Stateful**: Remembers position between iterations
3. **Lazy Evaluation**: Generates values on demand
4. **Reusable**: Can iterate multiple times (if `__iter__` resets state)

## Visual Representation

```
Countdown Object
┌───────────────────────┐
│ start: 5              │
│ current: (changes)    │
│                       │
│ __iter__()            │
│ __next__()            │
└───────────────────────┘
    ↑
    │
    └── For loop calls these methods automatically
```

## Common Mistakes

❌ Forgetting to reset state in `__iter__`:
```python
def __iter__(self):
    return self  # Without resetting current, can't iterate again
```

❌ Not raising `StopIteration`:
```python
def __next__(self):
    if self.current >= 0:
        self.current -= 1
        return self.current + 1
    # Missing StopIteration - will return None forever
```

## Practice Exercise

Create a `Range` class that works like Python's `range()`:

```python
class Range:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current < self.stop) or \
           (self.step < 0 and self.current > self.stop):
            value = self.current
            self.current += self.step
            return value
        raise StopIteration

# Test it
for num in Range(1, 10, 2):
    print(num)  # 1, 3, 5, 7, 9
```

## When to Make Classes Iterable

1. When your class represents a sequence/collection
2. For lazy evaluation of large datasets
3. When you want to use your objects in for-loops
4. For custom data structures (trees, graphs etc.)
5. When implementing generators as classes

## Advanced Usage

### Separate Iterator Class
```python
class CountdownIterator:
    def __init__(self, countdown):
        self.countdown = countdown
        self.current = countdown.start
    
    def __next__(self):
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        raise StopIteration

class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return CountdownIterator(self)
```

### Infinite Iterators
```python
class InfiniteCounter:
    def __init__(self):
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.current
        self.current += 1
        return value  # Never raises StopIteration
```

## Final Notes

- `__iter__` should return an iterator object
- `__next__` should return values and raise `StopIteration` when done
- The same object can be both iterable and iterator
- Iterators are single-use - create new ones for new iterations
- Follow Python's iterator protocol for seamless integration

Understanding iterable classes helps you create objects that work naturally with Python's iteration constructs like `for` loops, comprehensions, and generator expressions.