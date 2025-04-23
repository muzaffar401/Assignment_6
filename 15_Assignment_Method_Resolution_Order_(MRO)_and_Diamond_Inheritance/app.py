# A class banayi jisme show() method hai
class A:
    def show(self):
        print("Show from class A")

# B class banayi jo A ko inherit karti hai
class B(A):
    def show(self):
        print("Show from class B")

# C class banayi jo A ko inherit karti hai
class C(A):
    def show(self):
        print("Show from class C")

# D class banayi jo B aur C dono ko inherit karti hai
class D(B, C):  # MRO yahan important hai
    pass  # isme khud ka show() method nahi, lekin parent classes me hai

d = D()         # D class ka object banaya
d.show()        # D se show() call kiya — MRO decide karega kis class ka chalega

print(D.__mro__)  # ye dikhayega kis order me Python method dhundta hai

