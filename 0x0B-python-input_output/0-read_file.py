#!/usr/bin/python3
""" module that handles file reading """


def read_file(filename=""):
    """ reads a textfile """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
