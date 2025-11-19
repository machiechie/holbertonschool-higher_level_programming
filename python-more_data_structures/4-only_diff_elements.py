#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for el in set_1:
        newest_set = new_set.append(el)
        for el in set_2:
            if el not in newest_set:
                newest_set.append(el)
    return newest_set
