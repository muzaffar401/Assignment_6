# Sabse pehle Dog class banayenge
# class ek blue print hoti hai jisse object banate hain

class Dog:

    def __init__(self, name, breed):  # constructor banaya jisme 2 arguments liye
        self.name = name     # self ka use karke name variable store kiya
        self.breed = breed   # self ka use karke breed variable store kiya

    def bark(self):  # ye ek instance method hai (har dog ka apna bark hoga)
        print(f"{self.name} is barking!")  # dog ka naam use karke message print kiya
        print(f"{self.name} ki breed : {self.breed}") # isme dog ki breed 

dog1 = Dog("Tommy", "German Shepherd")  # Dog class ka object banaya
dog1.bark()  # object ke sath bark() method call kiya

