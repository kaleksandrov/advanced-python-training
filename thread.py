#!/usr/bin/env python3


import threading
import time

def thethread():
    print('Working')
    return


threads=[]
for i in range(5):
    t = threading.Thread(
            target=thethread
            )
    threads.append(t)

[thread.start() for thread in threads]
[thread.join() for thread in threads]

print('End!')
