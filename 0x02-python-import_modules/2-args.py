#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = 0
    args = sys.argv[1:]
    if len(args) == 1:
        print("{} argument:".format(len(args)))
    elif len(args) > 1:
        print("{} arguments:".format(len(args)))
    else:
        print("{} arguments.".format(len(args)))

    for j in range(len(args)):
        i = i + 1
        print(f"{i}: {args[j]}")
