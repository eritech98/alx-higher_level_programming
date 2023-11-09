#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all \
    integers tuple (<score>, <weight>)"""
    num = 0
    den = 0
    if len(my_list) == 0:
        return 0
    for elem in my_list:
        num += (elem[0] * elem[1])
        den += elem[1]

    return num / den
