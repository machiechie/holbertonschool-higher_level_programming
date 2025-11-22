#!/usr/bin/python3
def raise_exception():
    a = 5
    b = "blue"
    try:
        divv = a / b
    except TypeError:
        divv = None
    finally:
        return divv
