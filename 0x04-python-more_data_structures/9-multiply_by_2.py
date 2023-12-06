#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = {}
    for k, v in a_dictionary.items():
        n.update({k: v*2})
    return n
