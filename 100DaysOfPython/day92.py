from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 10

print(fx(10))
print(fx(20))
print(fx(15))

print(fx(10))
print(fx(20))
print(fx(15))
