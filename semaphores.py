#!/usr/bin/env python

from time import sleep
from threading import Thread, Semaphore
from random import randint

CUSTOMER_COUNT = 25
WAITERS_COUNT = 4

restaurant = Semaphore(WAITERS_COUNT)

def time_to_process():
    return randint(0,5)

def customer():
    print('Waiting on the queue...')
    with restaurant:
        print('Buying some stuff...')
        time_to_wait = time_to_process()
        sleep(time_to_wait)
    print('Done!')


customers = [Thread(target=customer) for i in range(CUSTOMER_COUNT)]
[customer.start() for customer in customers]
[customer.join() for customer in customers]
