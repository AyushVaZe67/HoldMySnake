class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a + b


a1 = Math(11)
a1.addtonum(2)
print(a1.num)
print(a1.add(1,2))
