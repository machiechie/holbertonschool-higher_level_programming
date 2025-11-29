#!/usr/bin/python3
"""Module that defines a function to convert an object to its JSON string representation."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    import json
    return json.dumps(my_obj)
