import threading
import time

def func1(s):
    print(f'Sleeping for {s} seconds')
    time.sleep(s)

func1(4)
func1(4)
func1(4)