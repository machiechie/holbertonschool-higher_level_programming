#!/usr/bin/python3
"""Module for serializing and deserializing data to and from JSON files."""

import json

def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load data from a file and deserialize it from JSON."""
    with open(filename, 'r') as f:
        return json.load(f)
