# Ham ek Employee naam ki class banayenge
# Jisme 3 type ke variables honge: public, protected, private

class Employee:
    
    def __init__(self, name, salary, ssn):
        self.name = name         # public variable - har jagah se access ho sakta hai
        self._salary = salary    # protected variable - convention kehta hai ke isse sirf class aur child class access kare
        self.__ssn = ssn         # private variable - isse sirf class ke andar access kiya ja sakta hai

emp1 = Employee("Ali", 50000, "123-45-6789")  # object banaya

print("Public (name):", emp1.name)       # ye chalega 
print("Protected (_salary):", emp1._salary)  # ye bhi chalega (but warn kiya jata hai) 
# print("Private (__ssn):", emp1.__ssn)    # ye error dega AttributeError: 'Employee' object has no attribute '__ssn'
# agar private variable ko access karna he to name mangling means ke rename attribute name with class
print("Private (__ssn) via name mangling:", emp1._Employee__ssn)  # ye chalega 


# Aap class ke andar ek method bana ke private variable ko safely return kara sakte ho:

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):  # public method
        return self.__ssn

emp1 = Employee("Ali", 50000, "123-45-6789")
print(emp1.get_ssn())  # ab private data safe way se mil raha hai ✅
