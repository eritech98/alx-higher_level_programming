#!/usr/bin/python3

"""
Defines inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class \
            that inherited (directly or indirectly) from the specified class ;\
            otherwise False.
    """
    if a_class is type(obj):
        return False

    return issubclass(type(obj), a_class)
