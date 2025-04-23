# sabse pehle ek decorator function banate hain
def log_function_call(func):  # yahan func woh function hai jisko decorate karna hai
    def wrapper():  # ek inner function banate hain jo actual kaam karega
        print("Function is being called")  # yeh print karega function se pehle
        func()  # phir original function ko call karega
    return wrapper  # wrapper ko return karte hain — ye replace karega original function ko

# ab ek simple function banate hain jisko hum decorate karenge
@log_function_call  # yeh decorator lagaya say_hello() ke upar
def say_hello():
    print("Hello, Muzaffar!")  # actual kaam yeh kar raha hai


# ab function ko call karte hain
say_hello()  # jab yeh chalega, pehle decorator ka message aayega
