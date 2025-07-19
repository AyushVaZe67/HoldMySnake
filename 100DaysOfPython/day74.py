class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y



s1 = Shape(12,12)
print(s1.area())