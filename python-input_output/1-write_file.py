#!/usr/bin/python3
"""Module for file operations: reading and writing text files."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8)"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
