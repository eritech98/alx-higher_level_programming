#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number."""
    mode_ = number % 10
    if number < 0:
        mode_ = (number * -1) % 10
    print("{}".format(mode_), end="")
    return mod
