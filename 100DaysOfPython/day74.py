class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,x):
        super().__init__(x, x)

    def area(self):
        return 3.1415 * super().area()




s1 = Shape(2,4)
print(s1.area())

c1 = Circle(6)
print(c1.area())