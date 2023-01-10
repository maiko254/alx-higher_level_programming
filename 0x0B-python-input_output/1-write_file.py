#!/usr/bin/python3
# 1-write_file.py
# Michael O Bonyo
"""Implements a file writer function"""


def write_file(filename="", text=""):
    """Writes a string to a file and returns number of characters written

    Args:
        filename (string): name of the file
        text (string): string to write to file
    Returns:
        the number of characters written to file
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        return a_file.write(text)
