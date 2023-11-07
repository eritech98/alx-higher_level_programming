#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element at index idx from a list my_list"""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
