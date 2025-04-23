# Step 1: Custom Exception banayi jo Exception class se inherit karti hai
class InvalidAgeError(Exception):  # class ka naam capital me
    pass  # abhi kuch nahi likha, lekin yeh custom exception ban gaya

# Step 2: function banaya jisme age check karenge
def check_age(age):
    if age < 18:
        # agar age 18 se kam ho to exception raise karenge
        raise InvalidAgeError("Age must be at least 18 to proceed.")
    else:
        print("Age is valid. You may proceed.")


# Step 3: try...except block se error handle karenge
try:
    # yahan tum koi bhi age test kar sakte ho
    check_age(16)  # yeh 18 se kam hai, to error aayegi
except InvalidAgeError as e:
    print("Caught an exception:", e)  # yeh chalega agar error raise hui

