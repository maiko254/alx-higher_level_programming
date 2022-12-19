#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    n = 0
    for index in range(0, x):
        try:
            print(my_list[index], end="")
            n += 1
        except IndexError:
            break
    print()
    return (n)
