#!/usr/bin/env python3

operations = {
        'a': lambda a, b : a+b,
        's': lambda a, b : a-b,
        'm': lambda a, b : a*b,
        'd': lambda a, b : a/b,
}


data = [
        ('a', 4, 5),
        ('d', 0, 3),
        ('m', 4, 8),
        ('s', 1, 4),
]

print([operations[el[0]](el[1], el[2]) for el in data])
