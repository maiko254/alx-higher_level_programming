#!/usr/bin/python3
# 0-square.py
# Michael O Bonyo
"""Define a class square"""


class Square:
    """Create a square"""

    def __init__(self, size=0):
        """Initializing size value

        Args:
            size (int): Size of the created square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """get the current area of the square"""
        return (self.__size * self.__size)
