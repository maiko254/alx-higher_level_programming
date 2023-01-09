#!/usr/bin/python3
# 1-my_list.py
# Michael O Bonyo
"""Defines an inherited list class MyList"""


class MyList(list):
    """implements how to print sorted list"""

    def print_sorted(self):
        """prints list sorted in ascending order"""
        print(sorted(self))
