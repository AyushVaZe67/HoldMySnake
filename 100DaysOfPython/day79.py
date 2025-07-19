class Employee:
    def __init__(self,name):
        self.name = name

class Dancer:
    def __init__(self,dance):
        self.dance = dance

class EmployeeDancer(Employee, Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name


ed = EmployeeDancer('Salsa','Mia')
print(ed.name)
print(ed.dance)
