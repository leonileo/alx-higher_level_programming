#!/usr/bin/python3

""" This module add two integers 
    casting the numbers into integers.
    Their type have must be either int or float,
    if not it raises a TypeError: x must be an integer
"""

def add_integer(a, b=98):
    """ add_integer(1, 2)
        3
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return (int(a) + int(b))
    elif not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
