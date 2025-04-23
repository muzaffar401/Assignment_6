# Hum ek Counter class banayenge jo ye track karegi ke kitne objects ab tak ban chuke hain

class Counter:  # class ka naam capital letter se start hota hai (best practice)
    count = 0   # ye class variable hai, ye sab objects ke liye common hota hai (har object ka nahi, class ka hota hai)

    def __init__(self):  # jab bhi naya object banega to ye constructor chalega
        Counter.count += 1  # class variable ko update karne ke liye class ka naam use kiya, har object banne par +1 hoga

    @classmethod  # ye decorator lagate hain jab hume class method banana hota hai
    def show_count(cls):  # yahan cls ka matlab hota hai "class khud", jese self object ke liye hota hai, waise cls class ke liye hota hai
        print(f"Total objects created: {cls.count}")  # class variable ko access kiya cls.count se

# 3 objects banaye
c1 = Counter()
c2 = Counter()
c3 = Counter()

# ab count show karte hain
Counter.show_count()  # isko class ke naam se bhi call kar sakte hain


# output ayega Total objects created: 3