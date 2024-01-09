#!/usr/bin/python3
""" Implements class Student """


class Student:
    """ Creates a Student """
    def __init__(self, first_name, last_name, age):
        """ initializes object Student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if isinstance(attrs, list):
            for item in attrs:
                if type(item) == str:
                    for i in attrs:
                        if hasattr(self, i):
                            return ({i: getattr(self, i)})
        return (self.__dict__)

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for k, v in json.items():
            setattr(self, k, v)
