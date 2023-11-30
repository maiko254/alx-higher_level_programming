#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv
from sys import exit

if __name__ == "__main__":
    print(argv)
    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '+':
        print(f"{a} {op} {b} = {add(a, b)}")
    elif op == '-':
        print(f"{a} {op} {b} = {sub(a, b)}")
    elif op == '*':
        print(f"{a} {op} {b} = {mul(a, b)}")
    elif op == '/':
        print(f"{a} {op} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
