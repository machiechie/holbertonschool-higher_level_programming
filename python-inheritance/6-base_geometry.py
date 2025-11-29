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
