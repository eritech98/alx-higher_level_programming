#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    x = 0
    for i in set(my_list):
        x += i
    return x
