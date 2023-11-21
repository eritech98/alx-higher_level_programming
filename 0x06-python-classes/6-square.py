#!/usr/bin/python3
"""Square module"""


class Square:
    """Class Square that defines a square.

    Args:
        size - height of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(position, tuple) is False or len(position) != 2 \
            or isinstance(position[0], int) is False or \
                isinstance(position[1], int) is False or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """To retrieve position."""
        return self.__position

    @position.setter
    def position(self, position):
        """To set position."""
        if isinstance(position, tuple) is False or len(position) != 2 \
            or isinstance(position[0], int) is False or \
                isinstance(position[1], int) is False or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        y = 0
        while y < self.__position[1]:
            print()
            y += 1
        for i in range(self.__size):
            if self.__position[0] > 0 and self.__size > 0:
                print(" " * self.__position[0], end="")
            for x in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
