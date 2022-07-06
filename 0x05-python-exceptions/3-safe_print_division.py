#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        value of the division, otherwise none
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
