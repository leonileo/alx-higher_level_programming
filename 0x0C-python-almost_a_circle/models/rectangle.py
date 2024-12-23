#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ This rectangle class inherit from base class. """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        # validaion for width value
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

        # validation for height
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

        # validation for x
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

        # validation for y
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """A public getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, val):
        """A public setter for the private instance attribute width"""
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """A public getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, val):
        """A public setter for the private instance attribute height"""
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """A public getter for the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, val):
        """A public setter for the private instance attribute x"""
        if not isinstance(val, int):
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """A public getter for the private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, val):
        """A public setter for the private instance attribute y"""
        if not isinstance(val, int):
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """Returns the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints '#' to the stdout."""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assigns each argument to it's attribute."""
        if args:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if not args:
            for key, attr in kwargs.items():
                setattr(self, key, attr)

    def to_dictionary(self):
        """Returns the dictionary representaion of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
