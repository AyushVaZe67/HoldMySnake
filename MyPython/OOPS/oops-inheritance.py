class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        print(self.marks)

    def show_marks(self):
        print(f'{self.name} got {self.marks + 2} marks !!!')


class GraduateStudent(Student):
    def __init__(self, name, marks, stream):
        super().__init__(name,marks)
        self.stream = stream

    def show_marks(self):
        super().show_marks()
        print(f'{self.name} got {self.marks + 2} marks in {self.stream}!!!')

grad1 = GraduateStudent('Ayush',22,'AIDS')
print(grad1.stream)
print(grad1.name)

grad1.show_marks()

