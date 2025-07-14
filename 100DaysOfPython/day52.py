# x = int(input('Enter num:'))
# print((lambda x: x ** 2)(5))
# print((lambda x,y : (x+y)/2)(5,9))

avg = (lambda x,y : (x+y)/2)

def f1(avg1,value):
    return avg1 + value

print(f1(avg(5,7),10))