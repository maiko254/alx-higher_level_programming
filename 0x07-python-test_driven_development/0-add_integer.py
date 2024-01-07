#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Addition of 2 integers

    :param a: The first integer or float.
    :param b: The second integer or float. Default is 98.
    :return: The addition of a and b as an integer.

    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
