#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
