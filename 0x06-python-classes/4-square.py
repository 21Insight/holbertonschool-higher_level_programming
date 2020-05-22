#!/usr/bin/python3
"""Creating a new class called Square"""


class Square:
    """class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size

    def area(self):
        """Method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting a new value"""
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
