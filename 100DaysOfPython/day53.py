from functools import reduce

def cube(x):
    return x ** 3

def filter_function(a):
    return a > 2

l1 = [1,2,3,4,5]

print(reduce(lambda x,y : x * y,l1))

# for i in range(len(l1)):
#     print(cube(l1[i]))

# print(list(map(cube,l1)))
#
# print(list(filter(filter_function,l1)))