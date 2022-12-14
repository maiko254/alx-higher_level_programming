#!/usr/bin/python3
def val(a):
    if a == 'I':
        return 1
    if a == 'V':
        return 5
    if a == 'X':
        return 10
    if a == 'L':
        return 50
    if a == 'C':
        return 100
    if a == 'D':
        return 500
    if a == 'M':
        return 1000


def roman_to_int(roman_string):
    res = 0
    i = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    while(i < len(roman_string)):
        s1 = val(roman_string[i])

        if (i + 1 < len(roman_string)):
            s2 = val(roman_string[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res
