# Exercise 89 - Generator for Fibonacci Sequence
# Write a Python generator to yield Fibonacci numbers up to a specified limit.

def fibonacci_generator(limit: int):
    current = 0
    next = 1
    while current < limit:
        yield current
        current, next = next, current + next

