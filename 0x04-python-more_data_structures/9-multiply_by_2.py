#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {x: value*2 for x, value in a_dictionary.items()}
    return res
