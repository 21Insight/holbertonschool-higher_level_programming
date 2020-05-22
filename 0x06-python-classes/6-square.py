#!/usr/bin/python3
"""Creating a new class called Square"""


class Square:
    """class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square with size attribute"""
        self.__size = size
        self.position = position

    def area(self):
        """Method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Method to retrieve the size"""
        return self.__size

    @property
    def position(self):
        """Method to retrieve the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setting a new value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setting a new value"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Method that prints the square"""

        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")

            for i in range(self.__size):

                for sp in range(self.__position[0]):
                    print(" ", end="")

                for j in range(self.__size):
                    print("#", end="")

                print("")
        else:
            print("")
