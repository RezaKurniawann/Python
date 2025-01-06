# Exercise 12 - Pythagorean Theorem
# Write a program that takes the lengths of two sides of a right triangle
# as input and returns the length of the hypotenuse using the Pythagorean theorem
# https://en.wikipedia.org/wiki/Pythagorean_theorem.
# Formula is c^2 = a^2 + b^2. Your program should return the value of c.
import math


def calculate_hypotenuse(a, b):
    # Your code should go here.
    c = a**2 + b**2 
    return math.sqrt(c)

    # if dont use math.sqrt
    # c = (a**2 + b**2) ** 0.5
    # return c 

