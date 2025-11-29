#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
 
    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
