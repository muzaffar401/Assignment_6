# Ham ek Bank class banayenge jisme ek class variable hoga 'bank_name'
# aur ek class method hoga 'change_bank_name()' jo bank ka naam change karega

class Bank:  # class ka naam capital letter se start hota hai (best practice)
    bank_name = "State Bank"  # yeh class variable hai, sab objects ke liye common hota hai

    @classmethod  # yeh decorator use hota hai jab hume class method banana hota hai
    def change_bank_name(cls, name):  # cls ka matlab hota hai class khud
        cls.bank_name = name  # class variable ko change kar diya naya naam se

# Pehle do object banaye Bank class ke
account1 = Bank()
account2 = Bank()

# Dono objects ka bank name check karte hain (same hoga)
print("before.........")
print(account1.bank_name)  # output: State Bank
print(account2.bank_name)  # output: State Bank

# Ab bank ka naam change karte hain class method se
Bank.change_bank_name("National Bank")

# Fir se check karte hain dono objects ka bank name
print("after..............")
print(account1.bank_name)  # output: National Bank
print(account2.bank_name)  # output: National Bank

# before.........
# State Bank
# State Bank

# after..............
# National Bank
# National Bank

