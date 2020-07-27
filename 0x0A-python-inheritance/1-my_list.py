#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """ Class that inherits the attributes"""

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
