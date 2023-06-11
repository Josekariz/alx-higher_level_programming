#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find multiples of 2 in a list."""
    mtpl = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mtpl.append(True)
        else:
            mtpl.append(False)

    return (mtpl)
