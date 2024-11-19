#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ This rectangle class inherit from base class. """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """A public getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, val):
        """A public setter for the private instance attribute width"""
        self.__width = val

    @property
    def height(self):
        """A public getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, val):
        """A public setter for the private instance attribute height"""
        self.__height = val

    @property
    def x(self):
        """A public getter for the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, val):
        """A public setter for the private instance attribute x"""
        self.__x = val

    @property
    def y(self):
        """A public getter for the private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, val):
        """A public setter for the private instance attribute y"""
        self.__y = val
