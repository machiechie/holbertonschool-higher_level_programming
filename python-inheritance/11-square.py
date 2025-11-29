#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
