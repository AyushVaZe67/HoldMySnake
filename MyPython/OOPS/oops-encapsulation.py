class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        print(self.__marks)

    def show_marks(self):
        print(f'{self.name} got {self.__marks + 2} marks !!!')

s1 = Student('Ayush',11)
s1.get_marks()
s1.show_marks()