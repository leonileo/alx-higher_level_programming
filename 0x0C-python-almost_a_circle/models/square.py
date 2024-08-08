#!/usr/bin/python3

""" This module contains a child class of ``` Rectangle ```
and grand child of Base. """

from models.rectangle import Rectangle


class Square(Rectangle):

    """ A class that inherit from the rectangle class. """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)
