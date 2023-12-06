#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
           'F': 4, 'N': 9, 'J': 40, 'K': 90, 'O': 400, 'P': 900}
    val = []

    if type(roman_string) != str or roman_string is None:
        return None

    if 'IV' in roman_string:
        roman_string = roman_string.replace("IV", "F")
    if 'IX' in roman_string:
        roman_string = roman_string.replace("IX", "N")
    if 'XL' in roman_string:
        roman_string = roman_string.replace("XL", "J")
    if 'XC' in roman_string:
        roman_string = roman_string.replace("XC", "K")
    if 'CD' in roman_string:
        roman_string = roman_string.replace("CD", "O")
    if 'CM' in roman_string:
        roman_string = roman_string.replace("CM", "P")

    for i in roman_string:
        for k, v in rom.items():
            if i == k:
                val.append(v)

    return sum(val)
