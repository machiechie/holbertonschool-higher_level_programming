#!/usr/bin/python3
"""Module for reading file contents."""


def read_file(filename=""):
    """Read and return the contents of a file.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string."""
    with open(filename, 'r') as file:
        content = file.read()
    return content
