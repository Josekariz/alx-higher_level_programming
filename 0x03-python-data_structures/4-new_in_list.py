#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element from a copy of the list at a certain index."""
    if idx in range(len(my_list)):
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
