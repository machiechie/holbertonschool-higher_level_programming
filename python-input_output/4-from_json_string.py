#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    import json
    return json.loads(my_str)
