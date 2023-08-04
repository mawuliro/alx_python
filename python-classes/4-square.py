#!/usr/bin/env python3
"""Define a clss Square"""

class Square:
    """This is a class for a square building
    Args:
        size(int): first parameter
    Attributes:
        size(int): first attribute
    """
    def __init__(self, size=0):
        
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Evaluate tha area of the square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)
    
    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
