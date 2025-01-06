# Exercise 22 - Sum Even Numbers
# Write a program that sums the even numbers from start to end.
# For example, if the start is 1 and the end is 5, the sum is 6 (2 + 4).

# Can you solve this once using a for loop and once using a while loop?


def sum_even_numbers(start, end):
    # Your code should go here.
    total = 0
    for number in range (start, end + 1):
        if number % 2 == 0:
            total += number
    return total
        

def sum_even_numbers (start, end):
    total = 0
    while start <= end:
        if start % 2 == 0:
            total += start
        start += 1
    return total
