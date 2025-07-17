class Employee:
    company_name = 'Google'
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02

    def showDetails(self):
        print(self.name , self.raise_amount, self.company_name)

emp1 = Employee('Ayush')
emp1.company_name = 'Amazon'
emp1.showDetails()

emp2 = Employee('Mia')
emp2.raise_amount = 0.01
emp2.showDetails()