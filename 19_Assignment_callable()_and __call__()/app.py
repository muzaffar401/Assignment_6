# class banayi jiska naam Multiplier hai
class Multiplier:
    def __init__(self, factor):  # constructor banaya
        self.factor = factor     # factor store kiya, jaise 3, 5, etc.

    # __call__ method banaya — jab object ko call karoge, ye method chalega
    def __call__(self, number):
        return self.factor * number  # input number ko factor se multiply karega


# Multiplier ka object banaya jisme factor 5 set kiya
m = Multiplier(5)

# check karte hain kya m object callable hai?
print(callable(m))  # True hona chahiye, kyunke __call__ method defined hai

# object ko function ki tarah call kiya — m(10) ka matlab 10 * 5
print(m(10))  # Output: 50
