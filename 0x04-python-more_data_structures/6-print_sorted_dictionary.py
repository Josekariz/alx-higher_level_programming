#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordList = list(a_dictionary.keys())
    ordList.sort()
    for i in ordList:
        print("{}: {}".format(i, a_dictionary.get(i)))
