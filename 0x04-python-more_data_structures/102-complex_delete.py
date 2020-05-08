#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for val_dc in list_keys:
        if value == a_dictionary.get(val_dc):
            del a_dictionary[val_dc]

    return (a_dictionary)
