#!/usr/bin/python3
""" Implements a file writer """


def write_file(filename="", text=""):
    """ writes to a utf-8 encoded file """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
