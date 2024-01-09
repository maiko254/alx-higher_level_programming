#!/usr/bin/python3
""" creates an object from a JSON file """
import json


def load_from_json_file(filename):
    """ reads a file and creates an object from the JSON representation """
    with open(filename, encoding="utf-8") as f:
        return (json.loads(f.read()))
