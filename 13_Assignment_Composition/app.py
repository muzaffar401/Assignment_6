# Engine class banayi jisme ek method hai start_engine()
class Engine:
    def start_engine(self):  # ye engine ka method hai
        print("Engine has started.")  # jab ye chale to ye message aaye

# Car class banayi jisme Engine ka object andar include kiya jaayega
class Car:
    def __init__(self, engine):  # jab car banti hai to engine ka object pass hota hai
        self.engine = engine  # engine ko car ke andar store kiya

    def start(self):  # car ka method banaya
        self.engine.start_engine()  # car ke zariye engine ka method chala diya

# engine ka object banaya
my_engine = Engine()

# car ka object banate waqt engine ka object diya
my_car = Car(my_engine)

# car ka method call kiya jo andar se engine ka method chalata hai
my_car.start()  # Output: Engine has started.
