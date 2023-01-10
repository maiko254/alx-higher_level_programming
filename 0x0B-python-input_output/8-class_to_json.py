#!/usr/bin/python3
# 8-class_to_json.py
# Michael O Bonyo
"""Returns the dictionary description for JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
       for JSON serialization of an object

       Args:
           obj (any): object to get dictionary
    """
    return obj.__dict__
