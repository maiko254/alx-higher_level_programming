#!/usr/bin/python3
# 5-save_to_json_file.py
# Michael O Bonyo
"""Implements text file writer using a JSON represetation"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (any): object to write to file
        filename (string): name of file to write to
    """
    import json

    with open(filename, 'w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
