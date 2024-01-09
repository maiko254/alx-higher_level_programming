#!/usr/bin/python3
""" Implements a json encoder """
import json


def to_json_string(my_obj):
    """ converts an object into its json representation """
    return (json.dumps(my_obj))
