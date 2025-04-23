# Ham ek Logger class banayenge
# Jab object banega to constructor chalega aur message print karega
# Jab object destroy hoga (ya end ho jayega) to destructor chalega aur message print karega

class Logger:  # class ka naam capital se start kiya (Logger)

    def __init__(self):  # yeh constructor hai, jab object banta hai to yeh method automatically call hota hai
        print("Logger object has been created.")  # message print kiya jab object create hua

    def __del__(self):  # yeh destructor hai, jab object destroy hota hai tab yeh method call hota hai
        print("Logger object has been destroyed.")  # message print kiya jab object delete hua

logger1 = Logger()  # object banaya, constructor call hoga
del logger1  # object delete kiya, destructor call hoga


# for testing
def test():
    temp = Logger()  # object bana qk ye function ke andar tha object jese hi function khatam hua to object destroy hogaya
    # Logger object has been created.
    print("Inside function")

test()  # function call kiya

# Logger object has been destroyed.
print("Outside function")

# output
# Logger object has been created.
# Logger object has been destroyed.
# Logger object has been created.
# Inside function
# Logger object has been destroyed.
# Outside function

