class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'

    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)




v1 = Vector(4,2,8)
print(v1)

v2 = Vector(2,7,3)
print(v2)

print(v1 + v2)
print(type(v1+v2))