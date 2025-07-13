ep1 = {1: 10, 2: 20, 3: 30, 4: 40}
ep2 = {5: 50, 6: 60}
ep1.update(ep2)

ep1.pop(5)
ep1.popitem()

print(ep1)

ep1.clear()
print(ep1)
