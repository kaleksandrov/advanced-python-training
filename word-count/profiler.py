import time

def now():
    return int(round(time.time() * 1000))

class Profiler(object):

    def __enter__(self):
        self.start = now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = now()

    def millis(self):
        return self.end - self.start
    def seconds(self):
        return self.millis() / 1000
