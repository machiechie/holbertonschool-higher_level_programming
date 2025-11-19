#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = None
    max_key = None
    for key, value in a_dictionary.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key
