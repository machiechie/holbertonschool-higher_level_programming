#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance.

        If attrs is a list of strings, only include those attributes.
        Otherwise, return all attributes.

        Args:
            attrs (list, optional): list of attribute names to include
        """
        if attrs is None:
            # Return all attributes
            return self.__dict__
        
        # Return only attributes in attrs that exist in instance
        result = {}
        for key in attrs:
            if key in self.__dict__:
                result[key] = self.__dict__[key]
        return result
