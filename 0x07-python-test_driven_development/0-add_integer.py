#!/usr/bin/python3

# 0-add_integer.py

"""This modlue has one function that adds two arguments by checking
their types. The provided arguments must have a type of either
integers or float, otherwise the function will raise a TypeError
exception. If one of the arguments has a type of float it will
cast them into integers and return the addition of the arguments."""


def add_integer(a, b=98):
    """Checks the types of the two arguments,
    then return their summation.
    """
    if (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    elif (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')
    else:
        if (type(a) is float('inf') or type(a) is float('-inf')):
            raise OverflowError('cannot convert float infinity to integer')
        elif (type(b) is float('inf') or type(b) is float('-inf')):
            raise OverflowError('cannot convert float infinity to integer')
        elif(type(a) is float):
            a = int(a)
        elif(type(b) is float):
            b = int(b)
        return(a + b)
