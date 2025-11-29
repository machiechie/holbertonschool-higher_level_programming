#!/usr/bin/python3
"""Module for testing class to JSON serialization function."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.
    """
    return obj.__dict__
