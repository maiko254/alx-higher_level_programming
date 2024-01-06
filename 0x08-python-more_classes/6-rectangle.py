#!/usr/bin/python3
# 0-rectangle.py
# Michael O Bonyo
"""Define a class Rectangle"""


class Rectangle:

    number_of_instances = 0

    """Creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing width and height value


        Args:
            width (int): width of the created rectangle
            height (int): height of created rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves and sets the instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves and sets the instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets the area of the created rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates the perimeter of the created rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Returns the printable representation of the Rectagle"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            r = []
            for i in range(self.__height):
                [r.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    r.append("\n")
            return ("".join(r))

    def __repr__(self):
        """Returns the printable representation that can recreate Rectangle"""

        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes an instance of object Rectangle"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
