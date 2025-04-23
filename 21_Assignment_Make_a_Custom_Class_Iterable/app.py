# Step 1: Countdown class banayi jisme start number ho
class Countdown:
    def __init__(self, start):
        self.start = start  # start se countdown start hoga

    # Step 2: __iter__ method banaya — yeh method iterable banata hai
    def __iter__(self):
        self.current = self.start  # current ko start pe set kiya
        return self  # apne aap ko return karenge, taake next() method use ho sake


    # Step 3: __next__ method banaya — yeh method countdown karega
    def __next__(self):
        if self.current > 0:
            self.current -= 1  # countdown ho raha hai
            return self.current  # current number return hoga
        else:
            raise StopIteration  # jab 0 pe pahuch jayega, iteration stop ho jayega


# object banaya jisme countdown start hai 5 se
countdown = Countdown(5)

# for-loop me object use kiya
for number in countdown:
    print(number)  # yeh 5 se countdown karega
