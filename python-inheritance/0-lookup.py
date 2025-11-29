#!/usr/bin/python3
"""A simple function to look up the attributes of an object."""


def lookup(obj):
    """Return the list of attributes of the given object."""
    return dir(obj)
