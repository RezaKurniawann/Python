# Exercise 20 - Grade Result
# Write a program that take an integer between 0 and 100
# and returns the grade result based on the following rules:
# 1. “A” if grade is between 90 and 100
# 2. “B” if grade is between 80 and 89
# 3. “C” if grade is between 70 and 79
# 4. “Not Pass” if grade is less than 70


def grade_result(grade):
    # Your code should go here.
    if grade >= 90 and grade <= 100:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    else:
        return "Not Pass"
