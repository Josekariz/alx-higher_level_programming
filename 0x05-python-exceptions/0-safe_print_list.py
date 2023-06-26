#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.
    
    Returns the number of elements printed.
    """
    count = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
