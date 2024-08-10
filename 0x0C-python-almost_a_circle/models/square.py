#!/usr/bin/python3

""" This module contains a child class of ``` Rectangle ```
and grand child of Base. """

from models.rectangle import Rectangle


class Square(Rectangle):

    """ A class that inherit from the rectangle class. """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter func for size """
        return size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.height = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)
