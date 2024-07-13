#!/usr/bin/python3

""" Module 0-add_integer 
    contain one method and accept two values of int or float types
    casting the numbers into integers.
    returns an int sum
"""

def add_integer(a, b=98):
    """
        Return the summation of two argument
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return a +b
