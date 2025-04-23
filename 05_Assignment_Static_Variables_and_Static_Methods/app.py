# Ham ek MathUtils naam ki class banayenge
# jisme ek static method hoga 'add' jo do numbers ka sum karega
# is class me na koi instance variable hoga (self) aur na hi class variable (cls)

class MathUtils:  # class banayi jiska naam MathUtils rakha (math wale kaam ke liye)

    @staticmethod  # yeh decorator batata hai ke yeh static method hai ye sirf logics handle karta he iska class or object se kuch lena dena nhi hota
    def add(a, b):  # yeh method sirf do parameters lega (a aur b)
        return a + b  # in dono ka sum return karega
    
# static method ko use karne ke liye object banane ki zarurat nahi hai
result = MathUtils.add(10, 5)  # direct class ke naam se call kiya

print("Sum is:", result)  # Output: Sum is: 15


# output
# Sum is: 15

#second example ye calculator class jisme hammne static method banaya phir just call karwaya 

class Calculator:
    @staticmethod
    def multiply(x, y):
        return x * y

print(Calculator.multiply(4, 3))  

# Output: 12

