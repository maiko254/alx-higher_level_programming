#!/usr/bin/python3
""" Implements base class for the module """


class Base:
    """ Manages id attribute for all child classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instance of Base object with an id attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
