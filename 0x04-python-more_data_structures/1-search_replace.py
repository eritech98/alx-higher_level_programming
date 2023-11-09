#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.
    @my_list is the initial list.
    @search is the element to replace in the list.
    @replace is the new element."""

    new = []
    for i in my_list:
        if i == search:
            i = replace
        new.append(i)

    return new
