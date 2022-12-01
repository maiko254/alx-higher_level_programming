#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    res = 0
    args = sys.argv[1:]

    for i in range(len(args)):
        res = res + int(args[i])
    print(res)
