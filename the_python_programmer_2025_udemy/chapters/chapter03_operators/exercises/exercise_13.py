# Exercise 13 - Add Without Plus Operator
# This program below adds two numbers without using the '+' operator.

# There is a bug in the code below. Find it and fix it.

def add_without_plus_operator(a, b):
    # Continue the loop until there is no carry (b becomes 0)
    while b != 0:
        # Calculate the carry (AND operation)
        data = a & b
        # Calculate the sum without carry (XOR operation)
        a = a ^ b
        # Right shift the carry to apply it to the next bit
        b = data << 1  # Use left shift instead of right shift for carry handling

    return a
