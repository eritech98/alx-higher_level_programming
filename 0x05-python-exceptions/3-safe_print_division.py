#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result."""
    res = None
    try:
        if b == 0:
            raise ZeroDivisionError
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(res))
        return res
