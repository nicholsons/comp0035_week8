"""
Calculator containing basic math operations with functions rather than a class structure.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def divide(first_term, second_term):
    if second_term == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return first_term / second_term


def multiply(first_term, second_term):
    return first_term * second_term


