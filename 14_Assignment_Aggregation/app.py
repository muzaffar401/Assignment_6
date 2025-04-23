# Employee class banayi jisme name attribute hai
class Employee:
    def __init__(self, name):
        self.name = name  # employee ka naam set kiya

    def show(self):
        print(f"Employee Name: {self.name}")  # naam print karne ka method

# Department class banayi jisme employee object ko accept kiya
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name  # department ka naam
        self.employee = employee    # employee object ko store kiya (aggregation)

    def show_details(self):
        print(f"Department Name: {self.dept_name}")
        self.employee.show()  # department ke zariye employee ka method call

# Pehle employee object banaya
emp1 = Employee("Muzaffar")

# Fir department banaya aur usme employee object diya
dept1 = Department("IT", emp1)

# Details dikhate hain
dept1.show_details()
