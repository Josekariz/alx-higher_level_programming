#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific index."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
