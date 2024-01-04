#!/usr/bin/python3
# 0-rectangle.py
# Michael O Bonyo
"""Define a class Rectangle"""


class Rectangle:
    """Creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing width and height value


        Args:
            width (int): width of the created rectangle
            height (int): height of created rectangle
        """
        self.width = width
        self.height = height

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
