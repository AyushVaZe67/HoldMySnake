class Employee:
    company = 'Apple'
    def show(self):
        print(self.name , self.company)

    @classmethod
    def change(cls,newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = 'Ayush'
e1.show()