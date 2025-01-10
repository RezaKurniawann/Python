# Exercise 91 - Decorator
# Create a decorator @time_this that measures and prints the time taken for a function to execute.

from time import time
import logging
 
 
def time_this(func):
 
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        logging.info(f"Time taken to execute {func.__name__}: {end - start} seconds")
        return result
 
    return wrapper
