import time
import threading

class Timer:

    def __init__(self, callback, interval):
        self.callback = callback
        self.interval = interval
        self.thread = threading.Thread(target=self.timer_func)
    
    def start(self):
        self.thread.start()

    def timer_func(self):
        timing = time.time()
        while True:
            if time.time() - timing > self.interval:
                timing = time.time()
                self.callback()