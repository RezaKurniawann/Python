# Exercise 65 - Custom Exception
# Write a function that raises a custom exception called `NegativeValueError`
# if the input number is negative. If the number is positive, return the number.


# Implement the `NegativeValueError` class here.

class NegativeValueError(Exception):
    pass


def check_positive(number: int) -> int:
    if number < 0:
        raise NegativeValueError("The number is negative.")
    return number
