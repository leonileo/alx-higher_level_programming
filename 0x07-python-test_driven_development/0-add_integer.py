#!/usr/bin/python3
# 0-add_integer.py
""" Defines an integer addition function. """

def add_integer(a, b=98):
    """ Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    else:
        return(int(a) + int(b))
