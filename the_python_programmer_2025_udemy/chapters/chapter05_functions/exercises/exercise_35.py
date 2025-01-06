# Exercise 35 - Find Max
# Write a function that takes any number of arguments and returns the maximum value.
# Hint: Consider using *args syntax to handle a variable number of arguments.


# You may need to update the function signature. See tests/test_ch5.py for inspiration.
# DO NOT CHANGE THE FUNCTION NAME.


def find_max(*args):
    max_value = args[0]
    for arg in args:
        if max_value < arg:
            max_value = arg
    return max_value

#def find_max(*args):
#    return max (args)
