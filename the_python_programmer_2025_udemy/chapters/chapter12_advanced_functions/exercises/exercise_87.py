# Exercise 87 - Fibonacci Iterator
# Write a Python class that implements an iterator for generating the first n Fibonacci numbers.

class FibonacciIterator:
    def __init__(self, n: int):
        self.n = n
        self.count = 0
        self.current = 0
        self.next = 1
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        val = self.current
        self.current, self.next = self.next, self.current + self.next
        return val
   
