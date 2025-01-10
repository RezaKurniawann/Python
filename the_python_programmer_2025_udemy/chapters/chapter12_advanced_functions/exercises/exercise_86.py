# Exercise 86 - Even Number Iterator
# Write a Python class that implements an iterator for generating the first n even numbers.
class EvenNumberIterator:
    def __init__(self, n: int):
        self.n = n
        self.count = 0
        self.current = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        val = self.current
        self.current += 2
        return val

