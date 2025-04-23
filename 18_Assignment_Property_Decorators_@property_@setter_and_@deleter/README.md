# Understanding Property Decorators in Python - Beginner's Guide

## What are Property Decorators?

Property decorators (`@property`, `@setter`, `@deleter`) allow you to define getter, setter, and deleter methods for class attributes, enabling controlled access to private attributes.

## Baby Steps Explanation

### Step 1: Creating the Base Class with Private Attribute
```python
class Product:
    def __init__(self, price):
        self._price = price  # Protected/private attribute (convention)
```
- `_price` is marked as protected by convention (single underscore)
- Direct access is still possible but discouraged

### Step 2: Adding Getter with @property
```python
    @property
    def price(self):
        print("Getting price value")
        return self._price
```
- `@property` decorates the getter method
- Allows accessing `price` like an attribute (`obj.price`)
- Can add validation/logging before returning value

### Step 3: Adding Setter with @price.setter
```python
    @price.setter
    def price(self, value):
        print("Setting new price")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
```
- Setter is decorated with `@price.setter`
- Called when assigning to `price` (`obj.price = new_value`)
- Can validate new values before setting

### Step 4: Adding Deleter with @price.deleter
```python
    @price.deleter
    def price(self):
        print("Deleting price attribute")
        del self._price
```
- Deleter is decorated with `@price.deleter`
- Called when deleting `price` (`del obj.price`)
- Can clean up related attributes

### Step 5: Using the Property
```python
# Create product
p = Product(100)

# Get price (uses @property)
print(p.price)  # Output: Getting price value \n 100

# Set price (uses @price.setter)
p.price = 150   # Output: Setting new price

# Try invalid price
try:
    p.price = -50  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Delete price (uses @price.deleter)
del p.price     # Output: Deleting price attribute
```

## Key Benefits of Properties

1. **Encapsulation**: Control access to internal data
2. **Validation**: Validate values before setting
3. **Computed Attributes**: Calculate values on access
4. **Backward Compatibility**: Change implementation without breaking code
5. **Clean Syntax**: Access like attributes, not methods

## Visual Representation

```
Product Object
┌───────────────────────┐
│ _price: 100           │
│                       │
│ @property             │
│   price() (getter)    │
│                       │
│ @price.setter         │
│   price() (setter)    │
│                       │
│ @price.deleter        │
│   price() (deleter)   │
└───────────────────────┘
```

## Common Mistakes

❌ Forgetting to define property before setter/deleter:
```python
@price.setter  # Error - price property not defined yet
def price(self, value):
    pass
```

❌ Using same name for attribute and property:
```python
self.price = price  # Creates infinite recursion if property exists
```

## Practice Exercise

Create a `Temperature` class with:
1. Private `_celsius` attribute
2. Property `celsius` with getter/setter
3. Property `fahrenheit` that computes from celsius

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Test it
temp = Temperature(0)
print(temp.fahrenheit)  # 32.0
temp.celsius = 100
print(temp.fahrenheit)  # 212.0
```

## When to Use Properties

1. When you need to validate attribute values
2. For computed/derived attributes
3. To maintain invariants in your data
4. When you might need to change internal representation later
5. For attributes that require side effects when accessed/changed

## Advanced Usage

### Read-only Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

# radius can be read but not modified
```

### Property Documentation
```python
class Product:
    @property
    def price(self):
        """The price property controls product cost."""
        return self._price
```

## Final Notes

- Properties provide Pythonic way to implement getters/setters
- They maintain the simplicity of attribute access
- Enable you to add behavior to attribute access
- Follow the principle of uniform access
- Widely used in Python libraries and frameworks

Understanding properties helps you write more robust and maintainable classes by properly encapsulating your data while maintaining clean attribute-style access syntax.