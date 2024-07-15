#!/usr/bin/python3

""" This module return attribute and methods as a list """

def lookup(obj):
    """ This function recieve an argument and
        returns a list of methods and atribute of the argument.
    """
    ob = list(dir(obj))
    return(ob)
