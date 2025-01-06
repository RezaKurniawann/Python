# Exercise 24 - Calculate Total Length
# Write a program that calculates the total length of all words in a list.
# For example, given the list ['hello', 'world'], the total length is 10.


def calculate_total_length (words):
    total = 0
    for word in words:
        total += len(word)
    return total
