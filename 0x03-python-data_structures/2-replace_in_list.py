#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element from a list at a certain index."""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list to avoid modifying the original
    my_list[idx] = element
    return my_list
