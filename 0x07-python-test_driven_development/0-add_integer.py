#!/usr/bin/python3

"""
This module provides one function called
``add_integer()``.
which returns the summation of the provided arguments.
"""


def add_integer(a, b=98):
    """ This functions adds the provided arguments.
    add_integer(1, 3)
    4 """
    if (not isinstance(a, (int, float)) or a == float('inf') or
       a == float('-inf') or a != a):
        raise TypeError('a must be an integer')
    if (not isinstance(b, (int, float)) or b == float('inf') or
       b == float('-inf') or b != b):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
