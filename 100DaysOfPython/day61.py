class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f'Name: {self.name} and id: {self.id}')

class Programmer(Employee):
    def showLanguage(self):
        print('The default language is Python')

e = Employee('Ayush',12)
e.showDetails()
e2 = Programmer('Ayush',45)
e2.showLanguage()