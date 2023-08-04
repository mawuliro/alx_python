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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Evaluate tha area of the square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)
