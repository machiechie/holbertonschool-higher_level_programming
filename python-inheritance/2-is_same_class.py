#!/usr/bin/python3
"""Module for checking if an object is exactly an instance of a specified class."""

def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class."""
    if isinstance(obj, a_class):
        return True
    return False
