#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    scr = 0
    wgh = 0

    for avg in my_list:
        scr += avg[0] * avg[1]
        wgh += avg[1]

    return (scr / wgh)
