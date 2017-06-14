#!/usr/bin/env python3

import struct

PNG_HEADER=b"\x89PNG\r\n\x1a\n"
CHUNK_SIZE=4096


def print_binary_file(filename):
    with open(filename, 'rb') as f:
        for chunk in f.read(CHUNK_SIZE):
            print(chunk, end=' ')


def check_if_png(filename):
    with open(filename, 'rb') as f:
        header = f.read(8)
        f.seek(16)
        dimensions = f.read(8)
        if header == PNG_HEADER:
            print('This is a valid PNG file!!')
            width,height=struct.unpack(">2L", dimensions)
            print("Dimensions: {} x {}".format(width, height))
        else:
            raise Exception('Not a PNG file!!')


if __name__=='__main__':
    print_binary_file('img.png')
    check_if_png('img.png')
