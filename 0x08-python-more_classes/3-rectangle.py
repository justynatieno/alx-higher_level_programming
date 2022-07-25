#!/usr/bin/python3


"""Defines a class Rectangle."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value
        Args:
            value (int): the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """Retrieves the width of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value
        Args:
            value (int) the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the Rectangle."""
        if self.__width == 0 | self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
