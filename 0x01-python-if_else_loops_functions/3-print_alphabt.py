#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 113 or letter == 101:
        continue
    print("{}".format(chr(letter)), end="")
