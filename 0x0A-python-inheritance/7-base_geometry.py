#!/usr/bin/python3

"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    The BaseGeometry class.
    """
    def area(self):
        """
        Raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.

        Args:
            name: name of the value.
            value: the value.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
