#!/usr/bin/python3
""" Implements a file writer """
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a textfile using its json representation """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
