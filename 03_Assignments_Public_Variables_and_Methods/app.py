# Ham ek Car class banayenge jisme public variable 'brand' hoga 
# aur ek public method 'start()' hoga jo print karega ke car start ho gayi hai

class Car:  # class ka naam capital letter se likhte hain (best practice)
    def __init__(self, brand):  # constructor banaya jo jab object banega tab chalega
        self.brand = brand  # yeh public variable hai (self.brand), isko bahar se access kiya ja sakta hai

    def start(self):  # yeh public method hai, isko bhi bahar se call kiya ja sakta hai
        print(f"{self.brand} car is starting...")  # brand ke sath message print karwa rahe hain

# Object banaya Car class ka aur brand diya "Toyota"
my_car = Car("Toyota")

# Public variable 'brand' ko access kiya
print(my_car.brand)  # output: Toyota

# Public method 'start()' ko call kiya
my_car.start()  # output: Toyota car is starting...

# Toyota
# Toyota car is starting...