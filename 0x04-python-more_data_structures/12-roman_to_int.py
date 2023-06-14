#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_num = 0

    for ch in reversed(roman_string):
        if ch not in rom_n:
            return 0

        current_num = rom_n[ch]

        if current_num < last_num:
            num -= current_num
        else:
            num += current_num

        last_num = current_num

    return num
