#!/usr/bin/python3
# 4-from_json_string.py
# Michael O Bonyo
"""Implements a JSON deserializer"""


def from_json_string(my_str):
    """Deserializes a JSON string and returns the object

    Args:
        my_str (json string): object to deserialize
    Returns:
        deserialized object
    """
    import json

    return json.loads(my_str)
