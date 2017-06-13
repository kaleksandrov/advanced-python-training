#!/usr/bin/env python3

import time

def now():
    """Gives the current time into milliseconds"""
    return int(round(time.time() * 1000))

class Profiler(object):
    """A context manager that measures the time for execution its content"""

    def __enter__(self):
        self.start = now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = now()

    def millis(self):
        return self.end - self.start

    def seconds(self):
        return self.millis() / 1000
