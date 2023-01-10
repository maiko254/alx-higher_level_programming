#!/usr/bin/python3
# 2-append_write.py
# Michael O Bonyo
"""Implements function to append a string to a file"""


def append_write(filename="", text=""):
    """appends string to a text file and returns number of character addded

    Args:
        filename (string): name of the file
        text (string): text to append to end of the file
    Returns:
        the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as a_file:
        return a_file.write(text)
