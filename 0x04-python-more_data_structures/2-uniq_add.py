#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_l = set(my_list)
    count = 0

    for n in uniq_l:
        count += n

    return(count)
