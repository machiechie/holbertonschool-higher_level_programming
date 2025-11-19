#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = []
    for i in a_dictionary:
        i = i ** 2
        new_dic.append(i)
    return new_dic
