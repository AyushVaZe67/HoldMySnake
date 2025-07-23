import threading
import time

def func1(s):
    print(f'Sleeping for {s} seconds')
    time.sleep(s)

# time1 = time.perf_counter()
# func1(4)
# func1(4)
# func1(4)
# time2 = time.perf_counter()
# print(time2-time1)

time1 = time.perf_counter()
t1 = threading.Thread(target=func1, args=[3])
t2 = threading.Thread(target=func1, args=[2])
t3 = threading.Thread(target=func1, args=[4])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(f'\n{time2-time1}')