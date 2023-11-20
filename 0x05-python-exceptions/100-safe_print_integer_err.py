#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer."""
    try:
        print("{:d}".format(value))
    except Exception as t:
        print("Exception: {}".format(t), file=sys.stderr)
        return False
    return True
