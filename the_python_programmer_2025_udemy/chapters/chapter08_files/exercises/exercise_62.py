# Exercise 62 - File Checker
# Check if the numbers in the file are sorted in ascending order.

# Example: file1.txt
# 1
# 2
# 3
#
# should return True.

# Example: file2.txt
# 1
# 3
# 2
#
# should return False.


def is_file_sorted(file_name: str) -> bool:
    numbers = []
    with open(file_name) as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers == sorted(numbers)
