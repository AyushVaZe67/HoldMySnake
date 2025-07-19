class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print('Sound made')


class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species='Dog')
        self.breed = breed

    def make_sound(self):
        print('Bark!')

class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,species='Cat')

    def make_sound(self):
        print('Meow')


d1 = Dog('Manoj','Doberman')
d1.make_sound()

c1 = Cat('ManiMav')
c1.make_sound()


a1 = Animal('Dog','Dog')
a1.make_sound()

