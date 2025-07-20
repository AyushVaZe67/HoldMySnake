import time
def whileLopp():
    i = 0
    while i < 50000:
        i += 1

def forLoop():
    for i in range(50000):
        pass


init = time.time()
whileLopp()
print(time.time() - init)

init = time.time()
forLoop()
print(time.time() - init)


print(time.time())

t1 = time.localtime()
print(t1)