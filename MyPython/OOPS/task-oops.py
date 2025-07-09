class Student:
    def __init__(self,full_name,roll_no,percentage):
        self.name = full_name
        self.percentage = percentage
        self.roll = roll_no

    def details(self):
        print(self.name , self.roll)

    def show_percentage(self):
        print(f'{self.name} has {self.percentage}% with roll no {self.roll}')



student1 = Student('Ayush',17,98)
student2 = Student('Mia',18,69)
student1.show_percentage()
student2.show_percentage()

print(student1.__dict__)