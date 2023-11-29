#!/usr/bin/python3

"""Module with the matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for elem in matrix:
        if not isinstance(elem, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        len_list = len(matrix[0])
        if len(elem) != len_list:
            raise TypeError("Each row of the matrix must have the same size")
        for i in elem:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    outer_list = []

    for elem in matrix:
        inner_list = []
        for i in elem:
            inner_list.append(round(i / div, 2))
        outer_list.append(inner_list)

    return outer_list
