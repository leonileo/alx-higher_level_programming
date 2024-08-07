#!/usr/bin/python3

"""This module contains a Rectangle class that inherits from
The base model ```Base```."""

from models.base import Base


class Rectangle(Base):

    """ This class is an instance of the ```Base``` class."""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """ A getter function for private instance
        attribute ```__width```
        """
        return Rectangle.__width

    @width.setter
    def width(self, value):
        """ A setter function for private instance
        attribute ```__width```
        """
        Rectangle.__width = value
        return Rectangle.__width

    @property
    def height(self):
        """ A getter function for private instance
        attribute ```__height```
        """
        return Rectangle.__height

    @height.setter
    def height(self, value):
        """ A setter function for private instance
        attribute ```__height```
        """
        Rectangle.__height = value
        return Rectangle.__height

    @property
    def x(self):
        """ A getter function for private instance
        attribute ```__x```
        """
        return Rectangle.__x

    @x.setter
    def x(self, value):
        """ A setter function for private instance
        attribute ```__x```
        """
        Rectangle.__x = value
        return Rectangle.__x

    @property
    def y(self):
        """ A getter function for private instance
        attribute ```__y```
        """
        return Rectangle.__y

    @y.setter
    def y(self, value):
        """ A setter function for private instance
        attribute ```__y```
        """
        Rectangle.__y = value
        return Rectangle.__y
