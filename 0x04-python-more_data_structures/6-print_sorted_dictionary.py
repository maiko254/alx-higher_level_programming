#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = dict(sorted(a_dictionary.items()))
    for i, j in b.items():
        print("{}: {}".format(i, j))
