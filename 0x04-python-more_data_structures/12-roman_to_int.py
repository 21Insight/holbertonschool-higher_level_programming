#!/usr/bin/python3
def to_subtract(l_num):
    to_sub = 0
    max_list = max(l_num)

    for n in l_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    ls_rm = 0
    l_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= ls_rm:
                    num += to_subtract(l_num)
                    l_num = [rom_n.get(ch)]
                else:
                    l_num.append(rom_n.get(ch))

                ls_rm = rom_n.get(ch)

    num += to_subtract(l_num)

    return (num)
