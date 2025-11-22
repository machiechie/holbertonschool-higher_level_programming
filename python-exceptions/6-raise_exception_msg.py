#!/usr/bin/python3
def raise_exception_msg(message=""):
    message = "C is fun"
    try:
        print(message)
    except NameError:
        print("Python is cool")
