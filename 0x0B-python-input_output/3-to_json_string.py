#!/usr/bin/python3
# 3-to_json_string.py
# Michael O Bonyo
"""Implements a JSON representation of an object"""


def to_json_string(my_obj):
    """converts a string to a JSON representation

    Args:
        my_obj (string): object to convert to JSON representation
    Returns:
        the JSON representation of an object
    """
    import json

    return json.dumps(my_obj)
