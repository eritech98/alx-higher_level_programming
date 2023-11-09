#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    for i in {k: v for k, v in a_dictionary.items() if v == value}.keys():
        del a_dictionary[i]
    return a_dictionary
