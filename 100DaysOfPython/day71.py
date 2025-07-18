x = [12,34,56]
# print(dir(x))
# print(x.__add__)
class Person:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.age = 22

p1 = Person('Ayush',12000)
# print(p1.__dict__)

print(help(Person))