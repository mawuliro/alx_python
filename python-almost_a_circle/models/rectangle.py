#!/usr/bin/python3

"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width's value"""
        self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the value of the height"""
        self.__height = value

    @property
    def x(self):
        """Get the value of x coordinate"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set the value of x coordinate"""
        self.__x = value

    @property
    def y(self):
        """Get the value of y coordinate"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Set the value of y coordinate"""
        self.__y = value
    