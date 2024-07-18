#!/usr/bin/python3
# 0-add_integer.py

""" Module 0-add_integer 
    contain one method and accept two values of int or float types
    casting the numbers into integers.
    returns an int sum
"""

def add_integer(a, b=98):
    """ 
       Return the integer addition of a and b.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    else:
        if (a == 'int' or a == '-int'):
            raise OverflowError('cannot convert float infinity to integer')
        elif isinstance(a, float):
            a = int(a)
        elif isinstance(b, float):
            b = int(b)
        return(a + b)
