#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    e = 0
    try:
        while e < x:
            print(my_list[e], end="")
            e += 1
        print()
    except IndexError:
        print()
    return e
