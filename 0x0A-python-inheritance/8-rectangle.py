#!/usr/bin/python3
# 5-base_geometry.py
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
