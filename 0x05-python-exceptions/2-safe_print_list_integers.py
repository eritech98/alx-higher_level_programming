#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers."""
    e = 0
    e = 0
    try:
        while y < x:
            if isinstance(my_list[y], int):
                print("{:d}".format(my_list[y]), end="")
                e += 1
            y += 1
        print()
    except IndexError:
        raise
    return e
