#!/usr/bin/python3

"""
Defines the add_attribute function.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it’s possible.
    Args:
        obj - the object.
        name - the attribute name
        value - the attribute value
    """
    if '__dict__' in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
