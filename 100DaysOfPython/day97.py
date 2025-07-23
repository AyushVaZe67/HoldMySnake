import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func1(s):
    print(f'Sleeping for {s} seconds')
    time.sleep(s)
    return s

# time1 = time.perf_counter()
# func1(4)
# func1(4)
# func1(4)
# time2 = time.perf_counter()
# print(time2-time1)

        # time1 = time.perf_counter()
        # t1 = threading.Thread(target=func1, args=[3])
        # t2 = threading.Thread(target=func1, args=[2])
        # t3 = threading.Thread(target=func1, args=[4])
        #
        # t1.start()
        # t2.start()
        # t3.start()
        #
        # t1.join()
        # t2.join()
        # t3.join()
        #
        # time2 = time.perf_counter()
        # print(f'\n{time2-time1}')


def poolDemo():
    with ThreadPoolExecutor() as ex:
        # future1 = ex.submit(func1, 4)
        # future2 = ex.submit(func1, 6)
        # future3 = ex.submit(func1, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l1 = [1,2,3,4]
        results = ex.map(func1, l1)
        for i in results:
            print(i)


poolDemo()