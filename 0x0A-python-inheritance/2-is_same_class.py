#!/usr/bin/python3
# 2-is_same_class.py
# Michael O Bonyo
"""Defines a function to check class of object"""


def is_same_class(obj, a_class):
    """checks if object is instance of the specified class

    Args:
        obj (Any): the object to check
        a_class (type): the class to match type of object to
    Returns:
        if object matches class type - True
        if not - false
    """
    if type(obj) == a_class:
        return True
    return False
