class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle:
    def __init__(self,x):
        self.x = x

    def area(self):
        return 3.1415 * super().area()




s1 = Shape(12,12)
print(s1.area())

c1 = Circle(12)
print(c1.area())