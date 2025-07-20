import time
def whileLopp():
    i = 0
    while i < 500000:
        i += 1

def forLoop():
    for i in range(500000):
        pass


init = time.time()
whileLopp()
print(time.time() - init)

init = time.time()
forLoop()
print(time.time() - init)


print(time.time())