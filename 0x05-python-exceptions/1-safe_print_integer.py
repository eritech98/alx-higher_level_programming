#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with "{:d}".format()"""
    try:
        if isinstance(value, int) is False:
            raise ValueError
    except ValueError:
        return False
    print(value)
    return True
