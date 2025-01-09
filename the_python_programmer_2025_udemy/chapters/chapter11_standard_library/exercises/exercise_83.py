# Exercise 83 - Cached Fibonacci
# Given this fibonacci function, we want to cache the results using `functools.lru`.
from functools import lru_cache  # noqa: F401


@lru_cache(maxsize=128)
def compute_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)
