# Exercise 29 - GPA Calculator
# Write a program that calculates the GPA of a student.
# The program should take in the grades of the courses and return the GPA of the student.
# For example, given the grades [4, 3, 2], the function should return 3.0.


def gpa_calculator(grades):
    # Your code should go here.
    total_point = 0
    for point in grades:
        total_point += point
    return total_point / len (grades)

def gpa_calculator (grades):
    return sum (grades) / len (grades)
