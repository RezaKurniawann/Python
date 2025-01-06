# Exercise 23 - Largest Index
# Write a program that returns the index of the largest element in the list.
# For example, given the list [1, 2, 3, 4, 5], the function should return 4.


def largest_index(elements):
    # Your code should go here.

    largest = elements[0]
    index = 0

    for i in range (1, len (elements)):
        if elements [i] > largest:
            largest = elements [i]
            index = i
    return index

def largest_index (elements):
    largest = elements [0]
    index = 0
    for i, element in enumerate(elements):
        if element > largest:
            largest = element
            index = i
    return index
