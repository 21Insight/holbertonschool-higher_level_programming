#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l_ord = list(a_dictionary)
    l_ord.sort()
    for i in l_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
