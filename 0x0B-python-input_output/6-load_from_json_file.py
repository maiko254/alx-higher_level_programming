#!/usr/bin/python3
# 6-load_from_json_file.py
# Michael O Bonyo
"""Implements a JSON deserializer"""
import json


def load_from_json_file(filename):
    """Creates an object using a JSON file

    Args:
        filename (string): name of JSON file
    """
    with open(filename) as a_file:
        return json.load(a_file)
