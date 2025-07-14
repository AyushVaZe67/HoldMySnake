def cube(x):
    return x ** 3

l1 = [1,2,3,4,5]

# for i in range(len(l1)):
#     print(cube(l1[i]))

print(list(map(cube,l1)))
