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
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
