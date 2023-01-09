#!/usr/bin/python3
# 5-base_geometry.py
# Michael O Bonyo
"""Implents a class BaseGeometry"""


class BaseGeometry():
    """Defines BaseGeometry"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        
        Args:
            name (string): name
            value (int): value to validate
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
