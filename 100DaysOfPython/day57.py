class Person:
    name = 'Ayush VaZe'
    occupation = 'Student'
    age = 21

    def info(self):
        print(f'{self.name} is {self.occupation}')

a = Person()
a.name = 'Mia'
# print(a.name)
a.info()

b = Person()
b.name = 'Alex'
b.occupation = 'HR'
b.info()