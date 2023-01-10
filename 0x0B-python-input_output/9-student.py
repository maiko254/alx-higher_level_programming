#!/usr/bin/python3
# 9-student.py
# Michael O Bonyo
"""Implements class Student"""


class Student:
    """Defines a an object student"""

    def __init__(self, first_name, last_name, age):
        """Initialization of a student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
