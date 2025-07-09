class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show_marks(self):
        print(f'{self.name} got {self.marks + 2} marks !!!')


s1 = Student('Ayush',94)
s1.show_marks()

s1 = Student('Mia',67)
s1.show_marks()

s1 = Student('Daisy',34)
s1.show_marks()
