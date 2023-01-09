#!/usr/bin/python3
# 4-inherits_from.py
# Michael O Bonyo
"""Implements subclass checking function"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a subclass of the
       specified class

    Args:
        obj (any): object instance to check
        a_class: class to match if object type is instance of subclass
    Returns:
        if object is instance of subclass - True
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
