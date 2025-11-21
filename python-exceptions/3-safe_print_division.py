#!/usr/bin/python3
def safe_print_division(a, b):
    divv = None
    try:
        divv = a / b
    except ZeroDivisionError:
        divv = None
    finally:
        print("Inside result:{}".format(divv))
        return divv
