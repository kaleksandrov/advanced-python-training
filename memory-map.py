#!/usr/bin/env python3

import mmap
with open("phrase.txt", "w") as file:
    phrase='''Now is the time for all men
and women to come to the aid of their
country'''
    file.write(phrase)

with open("phrase.txt", "r+b") as file:
    map = mmap.mmap(file.fileno(), 0)
    print(map[4:6])
    map[4:6]=b"as"
    map.close()
