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

    @property
    def size(self):
        """To retrieve attribute size."""
        return self.__size

    @size.setter
    def size(self, size):
        """To set attribute size.

        Args:
            size - height of the square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
