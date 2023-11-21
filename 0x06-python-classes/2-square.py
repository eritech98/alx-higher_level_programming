#!/usr/bin/python3
"""Square module"""


class Square:
    """Class Square that defines a square.

    Args:
        size - height of the square.
    """
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
