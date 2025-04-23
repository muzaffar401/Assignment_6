# sabse pehle ek class decorator banate hain
def add_greeting(cls):  # yahan cls matlab jo class decorate hogi (jaise Person)
    
    # ek nayi method define karte hain jo class me add karenge
    def greet(self):
        return "Hello from Decorator!"  # jab ye method call hoga to ye message dega

    # ye greet method ko class me dynamically add kar dete hain
    cls.greet = greet
    
    return cls  # modified class ko return karte hain

# ab ek simple class Person banate hain
@add_greeting  # decorator lagaya — ye class me greet() method automatically daal dega
class Person:
    def __init__(self, name):
        self.name = name  # bas name attribute hai


# ab object banate hain Person class ka
p = Person("Muzaffar")

# ab greet() method bhi available hai — decorator ki wajah se
print(p.name)        # ye print karega name
print(p.greet())     # ye print karega "Hello from Decorator!"
