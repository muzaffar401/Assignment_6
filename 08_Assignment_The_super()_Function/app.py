# Ham ek Person class banayenge jisme ek constructor hoga
# Ye constructor name set karega

class Person: # ye parent class he
    def __init__(self, name):  # constructor me name parameter liya
        self.name = name       # self.name me value store ki
        print("Person constructor called")  # ye sirf check karne ke liye likha

# Ab ham ek Teacher class banayenge jo Person se inherit karegi
# Aur super() ka use karke parent class ka constructor bhi call karegi

class Teacher(Person):
    def __init__(self, name, subject):  # child class ka constructor
        super().__init__(name)         # parent class ka constructor call kiya using super()
        self.subject = subject         # apni class ka naya field subject banaya
        print("Teacher constructor called")  # sirf samajhne ke liye

teacher1 = Teacher("Sir Anas", "Python")  # Teacher class ka object banaya

print(f"Teacher Name : {teacher1.name}")
print(f"Subject : {teacher1.subject}") 

# output
# Person constructor called
# Teacher constructor called
# Teacher Name : Sir Anas
# Subject : Python


# ek or example

# Ham ek Employee class banayenge
# Jisme name aur salary store hoga constructor ke through

class Employee:
    def __init__(self, name, salary):  # constructor me 2 parameters lenge
        self.name = name               # name ko instance variable me store kiya
        self.salary = salary           # salary ko bhi store kiya
        print("Employee constructor called")  # check karne ke liye message

# Ab Manager class banayenge jo Employee se inherit karegi
# isme ek extra variable hoga: department
# aur super() ka use karke parent class ka constructor bhi call hoga

class Manager(Employee):
    def __init__(self, name, salary, department):  # child class ka constructor
        super().__init__(name, salary)             # parent class ka constructor call kiya
        self.department = department               # apna extra field set kiya
        print("Manager constructor called")        # message print kiya

manager1 = Manager("Muzaffar", 90000, "IT")
print("Name:", manager1.name)           # parent class ka variable
print("Salary:", manager1.salary)       # parent class ka variable
print("Department:", manager1.department)  # child class ka variable


# output
# Employee constructor called
# Manager constructor called
# Name: Muzaffar
# Salary: 90000
# Department: IT

