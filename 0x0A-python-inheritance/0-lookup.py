#!/usr/bin/python3
# 0-lookup.py
# Michael O Bonyo
"""Gets the list of available attributes and methods of an object"""


def lookup(obj):
    """Retrieves list of attriutes and methods of an object

    Args:
        obj: object to get its attributes and objects
    """
    return (dir(obj))
