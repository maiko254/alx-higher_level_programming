#!/usr/bin/python3
# Michael O Bonyo
""" module that handles file reading """


def read_file(filename=""):
    """ reads a textfile """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
