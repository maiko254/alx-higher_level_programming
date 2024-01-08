#!/usr/bin/python3
# 10-square.py
# Michael O Bonyo
"""implements class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
