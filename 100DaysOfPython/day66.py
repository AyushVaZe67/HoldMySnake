class Employee:
    def __init__(self,name):
        self.name = name

    def showDetails(self):
        print(self.name)

emp1 = Employee('Ayush')
emp1.name = 'Ayush1'
emp1.showDetails()