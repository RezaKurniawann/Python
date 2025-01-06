# Exercise 31 - Palindrome
# Write a function to check whether a string is palindrome or not

# A palindrome is a word that reads the same forward and backward.
# For example, "racecar" is a palindrome.

# Bonus: Can you also solve this using a recursive function?


# You may need to update the function signature. See tests/test_ch5.py for inspiration.
# DO NOT CHANGE THE FUNCTION NAME.

def is_palindrome(word: str) -> bool:
    return word == word[::-1]  # [::-1] is a clever syntax to reverse a string in Python


# Or using a recursive function
def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
