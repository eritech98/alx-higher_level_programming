#!/usr/bin/python3
def square_matrix_map(m=[]):
    return list(map(lambda x: list(map(lambda y: y**2, m[x])), range(len(m))))
