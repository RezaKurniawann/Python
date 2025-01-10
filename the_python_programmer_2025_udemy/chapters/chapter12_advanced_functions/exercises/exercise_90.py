# Exercise 90 - Counter Closure
# Write a Python closure that keeps track of how many times it has been called.

def counter():
    count = 0
 
    def inner():
        nonlocal count
        count += 1
        return count
 
    return inner
