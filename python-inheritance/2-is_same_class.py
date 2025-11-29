#!/usr/bin/python3
"""Module for checking if an object
is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    if isinstance(a_class, type) and type(obj) is a_class:
        return True
    return False
