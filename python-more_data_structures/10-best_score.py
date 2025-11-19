#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = None
    max_key = None
    for key, value in a_dictionary.items():
        if max_val is None or value > max_val:
            max_val = value
            max_key = key
    return max_key
