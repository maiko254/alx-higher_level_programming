#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    n = 0
    try:
        for index in range(0, x):
            print(my_list[index], end="")
            n += 1
        print()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    return n
