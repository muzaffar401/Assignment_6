# Product class banate hain
class Product:
    def __init__(self, price):  # constructor banaya
        self._price = price  # private variable _price banaya (underscore se denote karte hain)

    # @property decorator lagaya — ab price ko function ki tarah nahi, variable ki tarah access kar sakte hain
    @property
    def price(self):
        print("Getting price...")  # ye print karega jab price access hoga
        return self._price  # original value return karega


    # @price.setter decorator lagaya — isse price ko update kar sakte hain
    @price.setter
    def price(self, value):
        print("Setting price...")  # ye print karega jab price set hoga
        if value < 0:
            print("Price cannot be negative!")  # validation bhi laga sakte hain
        else:
            self._price = value  # naye value se update hoga

    # @price.deleter decorator lagaya — price ko delete karne ke liye
    @price.deleter
    def price(self):
        print("Deleting price...")  # ye print karega jab delete hoga
        del self._price  # _price attribute delete hoga


# Product ka object banaya
p = Product(150)

print(p.price)      # price ko read kiya (property use hui)
p.price = 200       # price ko update kiya (setter use hua)
del p.price         # price ko delete kiya (deleter use hua)
