#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item in a list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
