#!/usr/bin/env python3
def is_prime(number):
    if number > 0:
        for i in range(2, number):
            if number % i == 0:
                result = False
                break
            else:
                result = True
    else:
        result = False
    return result
