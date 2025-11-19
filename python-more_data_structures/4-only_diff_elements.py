#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for el in set_1:
        if el not in set_2:
            new_list.append(el)
    for el in set_2:
        if el not in set_1:
            new_list.append(el)
    return new_list
