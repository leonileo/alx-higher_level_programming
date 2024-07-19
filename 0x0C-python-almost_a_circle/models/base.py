#!/usr/bin/python3
""" base.py """

class Base:
    """ This is the base class, it recvieve one argument id.
       If the id is passed it'll add to the private attribute nb_objects..
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if (self.id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
