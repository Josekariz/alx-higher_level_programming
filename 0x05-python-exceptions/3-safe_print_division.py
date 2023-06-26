#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the sol division of a by b."""
    try:
        divided = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(divided))
    return (divided)
