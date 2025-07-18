# class Parent:
#     def parent_method(self):
#         print('Parent Method')
#
# class Child(Parent):
#     def parent_method(self):
#         print('Child\'s Parent Method')
#     def child_method(self):
#         print('Child Method')
#         super().parent_method()
#
#
# c_obj = Child()
# c_obj.child_method()
# c_obj.parent_method()

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

e1 = Employee('Ayush','12')
e2 = Programmer('Mia','13','Java')
print(e1.name,e1.id)
print(e2.name,e2.id,e2.lang)











