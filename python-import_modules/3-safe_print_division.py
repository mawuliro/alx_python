#!/usr/bin/env pytthon3
def safe_print_division(a, b):
    """
    Args:
        a: first int
        b: second int
    Returns:
        The return value. a / b
    """
    try:
        solution = a / b
    except ZeroDivisionError:
        solution = None
    finally:
        result = solution
        print("Inside result: {}".format(result))
