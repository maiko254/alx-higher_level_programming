#!/usr/bin/python3
# 3-is_kind_of_class.py
# Michael O Bonyo
"""Defines a class and class inheritance checking function"""


def is_kind_of_class(obj, a_class):
    """checks if object is instance of specified class or instance
       of class inherited from specified class

    Args:
        obj (Any): object to check
        a_class (type): class to match object type to
    Returns:
        if obj is instance of class or inherited instance of class: True
        otherwise: False
    """
    if isinstance(obj, a_class):
        return True
    return False
