#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return None
    sorted_list = sorted(my_list, reverse=True)
    return sorted_list[0]
