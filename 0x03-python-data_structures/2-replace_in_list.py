#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element from a list at a certain index."""
    if idx in range(len(my_list)):
        my_list[idx] = element
    return (my_list)
