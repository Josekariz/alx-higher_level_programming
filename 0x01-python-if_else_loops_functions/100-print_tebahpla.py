#!/usr/bin/python3

for c in range(ord('Z'), ord('A') - 1, -1):
    case = chr(c) if c % 2 == 0 else chr(c).lower()
    print(case, end="")
