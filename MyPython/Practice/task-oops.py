class Student:
    def __init__(self,full_name,roll_no):
        self.name = full_name
        self.roll = roll_no


student1 = Student('Ayush',17)
print(student1.name,student1.roll)