#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(new_list):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            divv = a / b
        except TypeError:
            return 0
            print("wrong type")
        except ZeroDivisionError:
            return 0
            print("division by 0")
        except IndexError:
            return 0
        print("out of range")
        finally:
            new_list.append(divv)
    return new_list
