#!/usr/bin/python3

""" This module has a function named lookup that returns the list of available attributes and methods of an object. """

def lookup(obj):
    """ This function recieve an argument and returns a list of methods and atribute of the argument. """
    ob = dir(obj)
    return(ob)
