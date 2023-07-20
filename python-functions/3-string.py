#!/usr/bin/env python3
def reverse_string(string):
    lists = []
    for i in string:
        lists.insert(0, i)
    return "".join(lists)
