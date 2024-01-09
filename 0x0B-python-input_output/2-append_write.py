#!/usr/bin/python3
""" Implements a file writer that appends data read to a file """


def append_write(filename="", text=""):
    """ writes to a file by appending read data """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
