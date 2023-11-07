#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list(my_list) at a specific position(idx)."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list
    new_list[idx] = element
    return new_list
