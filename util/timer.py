import time

class Timer:
    def __init__(self):
        self.start = time.time()

    def startT(self):
       self.start = time.time()

    def stop(self):
        end = time.time()
        print(end - self.start)