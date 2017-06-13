#!/usr/bin/env python3
"""Holds several genrators and iterators for walking through a file by char or by word"""

def words(filename, chunk_size):
    """Generator returning all the words contaned in a file."""
    word = []
    for char in Chars(filename, chunk_size):
        if char.isalpha():
            word.append(char)
        else:
            if word:
                yield ''.join(word)
                word = []


class Chars(object):

    """Iterator factory for getting the chars in a file one by one"""

    def __init__(self, filename, chunk_size=1):
        self.filename = filename
        self.chunk_size = chunk_size

    def __iter__(self):
        return CharIterator(self.filename, self.chunk_size)


class CharIterator(object):
    """Iterator that returns the content of a file char by char"""


    def __init__(self, filename, chunk_size=1):
        self.filename = filename
        self.chunk_size = chunk_size
        self.chunk = ''
        self.chunk_index = 0
        self.file = open(filename, 'r')


    def __next__(self):
        if len(self.chunk) == self.chunk_index:
            self.chunk = self.file.read(self.chunk_size)
            self.chunk_index = 0

            if not self.chunk:
                raise StopIteration()

        result = self.chunk[self.chunk_index]
        self.chunk_index += 1
        return result
