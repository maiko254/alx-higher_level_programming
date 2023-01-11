#!/usr/bin/python3
# 12-pascal_triangle.py
# Michael O Bonyo
"""Implements function that creates Pascal’s triangle"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing the
       Pascal’s triangle

    Args:
        n (int): number of rows in triangle
    Returns:
        list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n - 1):
        tr = triangle[-1]
        temp = [1]

        for i in range(len(tr) - 1):
            temp.append(tr[i] + tr[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
