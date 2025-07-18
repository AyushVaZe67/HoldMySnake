class Person:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(s1.split('-')[0],int(s1.split('-')[1]))



e1 = Person('Ayush',12345)
print(e1.name)
print(e1.salary)

s1 = 'Mia-12000'
e2 = Person.fromStr(s1)
print(e2.name)
print(e2.salary)