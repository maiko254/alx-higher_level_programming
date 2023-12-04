#!/usr/bin/python3
def no_c(my_string):
    st = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            st += i
    return st
