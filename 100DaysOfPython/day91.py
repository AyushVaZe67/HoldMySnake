def generator():
    for i in range(1,21):
        yield i


gen = generator()

for j in gen:
    if j % 2 == 0:
        print(j,end=' ')
