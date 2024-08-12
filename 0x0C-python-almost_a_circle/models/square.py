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
        """ Getter function for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the argument value to width """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns the arguments to attributes. """
        if args and len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)
