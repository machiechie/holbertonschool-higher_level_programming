#!/usr/bin/python3
"""Module for checking if an object is an instance or subclass of a given class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance or subclass of a_class."""
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
