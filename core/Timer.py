import time
import threading

def timer_func(callback):
    timing = time.time()
    while True:
        if time.time() - timing > 60.0:
            timing = time.time()
            callback()



def timer_start(callback):
    threading.Thread(target=lambda: timer_func(callback)).start()