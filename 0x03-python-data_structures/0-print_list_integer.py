#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for x in range(len(my_list)):
        # Format the integer as a decimal
        print("{:d}".format(my_list[x]))
