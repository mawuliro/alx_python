#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_iseq = [0, 1]
        while len(fib_iseq) < n:
            next_fib = fib_iseq[-1] + fib_iseq[-2]
            fib_iseq.append(next_fib)
        return fib_iseq
