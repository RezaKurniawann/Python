# Exercise 63 - How Many emails?
# Write a function that reads a file and returns the number of emails in the file.
#
# Example: emails.txt
#   test1@abc.com
#   test2@abc.com
#   fullname1
#   fullname2
#   test3@abc.com

# The function should return 3.
# A valid email address contains a single @ symbol.


def count_emails(file_name: str) -> int:
    with open (filename) as file:
        return sum (1 for line in file if "@" in line)

def count_emails (filename: str) -> int:
    with open (filename) as file:
        count = 0
        for line in file:
            if "@" in line:
                count += 1
        return count
