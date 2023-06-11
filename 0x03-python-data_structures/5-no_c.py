#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            new_string += x
    return new_string
print(no_c("Hello, World!"))  # Output: Hello, World!
print(no_c("Cats and dogs"))  # Output: ats and dogs
print(no_c("Coding in Python"))  # Output: Coding in Python
