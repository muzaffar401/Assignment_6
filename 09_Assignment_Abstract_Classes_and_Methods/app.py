# Ham abc module import karenge jo abstract classes banane me help karta hai
from abc import ABC, abstractmethod  # ABC = Abstract Base Class

# Ab ham Shape naam ki abstract class banayenge
# Isme ek abstract method area() banayenge
# abstract class ka matlab hota hai: isse object nahi banaya ja sakta

class Shape(ABC):  # ABC se inherit kiya matlab ab ye ek abstract class ban gayi
    
    @abstractmethod  # is decorator se ye method abstract ban gaya
    def area(self):  # area method banaya jisko har child class ko lazmi implement karna hoga
        pass  # yahan koi body nahi likhi, sirf structure diya gaya hai

# Rectangle class banayenge jo Shape class se inherit karegi
# Isme area() method ka implementation denge

class Rectangle(Shape):
    def __init__(self, width, height):  # rectangle ke liye width aur height chahiye
        self.width = width
        self.height = height
    
    def area(self):  # yahan area method implement kiya gaya
        return self.width * self.height

# s = Shape()  error dega TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'
rect1 = Rectangle(5, 10)
print("Area of Rectangle:", rect1.area())


# output 
# Area of Rectangle: 50