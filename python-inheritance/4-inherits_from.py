#!/usr/bin/python3
"""Module that defines a function to check class inheritance."""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
