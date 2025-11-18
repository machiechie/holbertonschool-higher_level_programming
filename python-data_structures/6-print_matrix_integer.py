#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print("{:d}".format(row), end="\n")
        for i in range(len(row)):
            print("{:d}".format(i), end=" ")
