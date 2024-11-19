#!/usr/bin/python3
"""Base class"""


class Base:
    """This class creates an id on creation of a new class."""

    __nb_objects = 0

    # instantiation
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
