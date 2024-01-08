#!/usr/bin/python3
# 5-base_geometry.py
# Michael O Bonyo
"""Implents a class BaseGeometry"""


class BaseGeometry():
    """Defines BaseGeometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (string): name
            value (int): value to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
