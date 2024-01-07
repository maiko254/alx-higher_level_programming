#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Divided all elements of a matrix """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    listlen = len(matrix[0])
    mt = []
    for m in range(len(matrix)):
        n = []
        if len(matrix[m]) != listlen:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix[m])):
            if not (isinstance(matrix[m][i], int) or
                    isinstance(matrix[m][i], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            n.append(round(matrix[m][i] / div, 2))
        mt.append(n)
    return (mt)
