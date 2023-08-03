#!/usr/bin/python3
import sys

n = len(sys.argv)
if n == 1:
    print("0 arguments.")
else:
    if n == 2:
        print("{:d} argument:".format(n - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(n - 1))
        for value in range(1, n):
            print("{:d}: {}".format(value, sys.argv[value]))
