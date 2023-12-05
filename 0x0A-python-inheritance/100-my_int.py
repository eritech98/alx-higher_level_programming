#!/usr/bin/python3

"""
Defines MyInt class.
"""


class MyInt(int):
    """
    Class MyInt - inherits from int.
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
