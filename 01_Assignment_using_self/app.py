# Hum self ka use karke ek Student class banayenge jisme name aur marks honge.
# Fir ek method display() banayenge jo student ki details print karegi.

# sabse pehle class banegi or class ek blue print he class se object banta he
class Student:  # class ka name hamesha capitalize me hoga 
    def __init__(self,name,marks): # jab bhi ham koi naya object banaenge to ye __init__() ka method bhi sath call hoga isse ham constructor kehte hen
        self.name = name # attribute ko access karne ke liye self use kiya jata he 
        self.marks = marks
        print(self) #object ka reference return karta he just for check
    def display(self): #display ka method banaya jisme hamne print karwaya he name or marks ko ab ye hame call karna hoga 
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student_1 = Student("Muzaffar",30) #ye hamne class ka object banaya 
student_1.display() # isko object ke sath call karne se print hoga name or marks

# output 
# <__main__.Student object at 0x000002951C31C650>
# Name: Muzaffar
# Marks: 30
