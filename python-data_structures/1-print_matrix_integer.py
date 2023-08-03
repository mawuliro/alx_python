#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for value in list:
            print("{}".format(value), end=" " if value != list[-1] else "")
        print()
