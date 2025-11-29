#!/usr/bin/python3
"""Module for reading file contents."""


def read_file(filename=""):
    """Read and return the contents of a file."""
    with open(filename, 'r') as file:
        content = file.read()
    print(content, end='')
