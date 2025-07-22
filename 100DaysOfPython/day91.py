def generator():
    for i in range(115):
        yield i


gen = generator()

for j in gen:
    print(j,end=' ')
