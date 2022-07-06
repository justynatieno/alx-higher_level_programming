#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return None
