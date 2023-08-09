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
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__height = height
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__x = x
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__y = y
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width's value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """Get the value of x coordinate"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set the value of x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y coordinate"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Set the value of y coordinate"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines the area of rectangle"""
        return (self.__height * self.__width)
    
    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        for coor_y in range(self.__y):
            print("")
        for h in range(self.__height):
            for coor_x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print('#', end="")
            print()
    
    def __str__(self):
        """Defines a printing string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                            self.__x,
                                                            self.__y,
                                                            self.__width,
                                                            self.__height))
    
    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
  
