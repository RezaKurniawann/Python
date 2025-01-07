# Exercise 42 - Count letters
# Write a function that takes a string and returns a dictionary
# with the count of each letter in the string.
# For example, the string "hello" should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

# Assume the string is all lowercase and contains no spaces.

def count_letters(word: str) -> dict[str, int]:
    result = {}
    for char in word:
        result[char] = result.get(char, 0) + 1
    return result
 
from collections import Counter
def count_letters(word: str) -> dict[str, int]:
    return dict(Counter(word))

