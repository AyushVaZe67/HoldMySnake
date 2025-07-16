class E1:
    def __init__(self,name,age):
        self.__name = name
        self._age = age

class E2(E1):
    def showAge(self):
        print(f'{self._age}')

e1 = E1('Ayush',22)
print(e1._E1__name)
e2 = E2('Mia',32)
print(e2._age)