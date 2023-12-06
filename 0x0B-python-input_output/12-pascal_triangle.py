#!/usr/bin/python3

"""
Has the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers \
            representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    big_list = [[1], [1, 1]]
    inner_list = [1, 1]

    for i in range(3, n + 1):
        lis = []
        for j in range(i - 2):
            lis.append(inner_list[j] + inner_list[j+1])
        inner_list = [1] + lis + [1]
        big_list.append(inner_list)
    return big_list
