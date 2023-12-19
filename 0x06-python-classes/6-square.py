#!/usr/bin/python3
# 0-square.py
# Michael O Bonyo
"""Define a class square"""


class Square:
    """Create a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing size value

        Args:
            size (int): Size of the created square
            position (tuple): co-ordinate of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets and sets the instance attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """gets and sets position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(x, int) for x in value) and
                all(x >= 0 for x in value)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """get the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
