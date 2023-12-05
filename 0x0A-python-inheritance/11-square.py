#!/usr/bin/python3

"""
Defines Square class.
"""
rectangle = __import__('9-rectangle')


class Square(rectangle.Rectangle):
    """
    The square class.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """
        Returns area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
