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

    def area(self):
        """ Calculate the area of a rectangle."""
        return self.width * self.height

    def display(self):
        """ Display the rectangle with the character ```#``` """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assign arguments to the public attrivute """
        if args and len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                    if i == 1:
                        self.width = args[1]
                    if i == 2:
                        self.height = args[2]
                    if i == 3:
                        self.x = args[3]
                    if i == 4:
                        self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return {
            'x': self.x,
            'y': self.y,
            'height': self.height,
            'width': self.width
        }

    # getter and setter functions

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
        # checks for the input type
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
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
        # checks for the input type
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')

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
        # checks for the input type
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')

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
        # checks for the input type
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')

        Rectangle.__y = value
        return Rectangle.__y
