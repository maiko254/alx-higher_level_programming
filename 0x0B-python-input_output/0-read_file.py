#!usr/bin/python3
# 0-read_file.py
# Michael O Bonyo
"""Implements a file reader"""


def read_file(filename=""):
    """defines how to read a UTF8 encoded text file

    Args:
        filename (string): name of file to read from
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
