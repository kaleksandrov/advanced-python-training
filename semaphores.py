#!/usr/bin/env python

from time import sleep
from threading import Thread, Semaphore
from random import randint

CUSTOMER_COUNT = 25
WAITERS_COUNT = 4

restaurant = Semaphore(WAITERS_COUNT)

def time_to_process():
    return randint(0,5)

def customer(number, time_to_process):
    print('[Customer-%d]: Waiting on the queue...'% number)
    with restaurant:
        print('[Customer-%d]: Buying some stuff...'% number)
        sleep(time_to_process)
    print('[Customer-%d]: Done!'% number)


customers = [Thread(target=customer, args=(i, time_to_process())) for i in range(CUSTOMER_COUNT)]
[customer.start() for customer in customers]
[customer.join() for customer in customers]
