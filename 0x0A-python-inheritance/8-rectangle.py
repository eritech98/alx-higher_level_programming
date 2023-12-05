#!/usr/bin/python3

"""
Defines Rectangle class.
"""
base_geometry = __import__('7-base_geometry')


class Rectangle(base_geometry.BaseGeometry):
    """
    Class Rectangle - inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
