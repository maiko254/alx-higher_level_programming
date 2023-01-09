#!/usr/bin/python3
# 9-base_geometry.py
# Michael O Bonyo
"""Implents a class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """initializes a new rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of Rectangle"""

        st = "[" + str(self.__class__.__name__) + "] "
        st += str(self.__width) + "/" + str(self.__height)
        return st
