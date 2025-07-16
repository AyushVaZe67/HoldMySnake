class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f'Name: {self.name} and id: {self.id}')


e = Employee('Ayush',12)
e.showDetails()