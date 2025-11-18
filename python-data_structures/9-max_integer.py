#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        print("None")
    else:
        maxs = sort(my_list)
        return(maxs[-1])
        
