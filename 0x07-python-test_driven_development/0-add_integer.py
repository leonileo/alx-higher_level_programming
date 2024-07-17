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
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    else:
        if type(a) == float:
            a = int(a)
        if type(b) == float:
            b = int(b)
        return a +b
