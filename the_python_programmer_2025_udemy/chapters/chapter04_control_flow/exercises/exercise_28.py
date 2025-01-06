# Exercise 28 - Reverse Digits
# Write a program that takes an integer as input and returns the integer with its digits reversed.
# For example, given the integer 123, the function should return 321.

def reverse_digits(number: int) -> int:
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10
    return reversed_number
 
def reverse_digits(number: int) -> int:
    return int(str(number)[::-1])
