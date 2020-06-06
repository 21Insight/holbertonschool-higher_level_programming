#!/usr/bin/python3
"""This module creates a Class Square"""


class Square:
    """Class Square with a constuctor method"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Args:
            size: size for __size attribute
            position: position for __position atributte
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Brings the area of square

        Returns:
            The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#'
        Prints the square in the given position (x, y)
        """
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        """
        brings the string version of a square

        Returns:
            square in form of a string
        """
        square_str = ""
        if self.__size > 0:
            for _ in range(self.__position[1]):
                square_str += "\n"
            for i in range(self.__size):
                for _ in range(self.__position[0]):
                    square_str += " "
                for _ in range(self.__size):
                    square_str += "#"
                if i < self.__size - 1:
                    square_str += "\n"
        else:
            square_str += ""
        return square_str

    @property
    def size(self):
        """
        getter function of size

        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function of size

        Args:
            value: value for __size attribute
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        getter function of position

        Returns:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter function of position

        Args:
            value: value for __position attribute
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value