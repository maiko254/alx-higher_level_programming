#!/usr/bin/python3
""" Implements a JSON decoder """
import json


def from_json_string(my_str):
    """ returns the object represented by a JSON string """
    return (json.loads(my_str))
