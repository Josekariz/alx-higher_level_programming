#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))  # Convert set back to a list
    num = sum(uniq_list)  # Use the sum() function directly

    return num
