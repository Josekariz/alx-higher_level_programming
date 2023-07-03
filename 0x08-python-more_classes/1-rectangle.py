#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """REp a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int):  W of the new rec.
            height (int): H of the new rec.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the W of the rec."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("W must be an integer")
        if value < 0:
            raise ValueError("W must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the H of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("H must be an integer")
        if value < 0:
            raise ValueError("H must greater or equal 0")
        self.__height = value
