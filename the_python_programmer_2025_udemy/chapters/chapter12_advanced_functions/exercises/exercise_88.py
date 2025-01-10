# Exercise 88 - Generator for Even Numbers
# Write a Python generator to yield the first n even numbers.

def even_numbers_generator(n: int):
    count = 0
    current = 0
    while count < n:
        yield current
        current += 2
        count += 1

