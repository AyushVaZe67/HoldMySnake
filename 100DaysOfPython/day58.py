class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f'My name is {self.name} and his/her age is {self.age}')


p1 = Person('Ayush',21)
p1.info()

p2 = Person('Alex',29)
p2.info()