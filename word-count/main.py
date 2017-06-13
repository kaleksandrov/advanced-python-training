#!/usr/bin/env python3

# TODO:
# 1. Ask about the encoding support

from profiler import Profiler
from pprint import pprint
from text import words


# FILE_NAME='test.log'
FILE_NAME='data/test3'
CHUNK_SIZE=5000000


def process_file(filename, register, chunk_size):
    for word in words(filename, chunk_size ):
        word = word.lower()
        register[word] = register.get(word, 0) + 1

if __name__=='__main__':
    register = {}
    filename = FILE_NAME
    chunk_size = CHUNK_SIZE

    p = Profiler()
    with p:
        process_file(filename, register, chunk_size)

    pprint(register)
    print("Time for processing the file %.3f seconds" % p.seconds())
