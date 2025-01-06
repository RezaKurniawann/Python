# Exercise 38 - Count Vowels Of A String
# Write a function that takes a string and returns the total number of vowels in the string.
# For example, the string "hello" should return 2.

# Bonus: Can you also solve this using a recursive function?


# You may need to update the function signature. See tests/test_ch5.py for inspiration.
#w DO NOT CHANGE THE FUNCTION NAME.
def count_vowels(word: str) -> int:
    vowels = "aiueo"
    return sum(1 for char in word if char.lower() in vowels)

def count_vowels(word: str) -> int:
    vowels = "aiueo"
    if not word:
        return 0
    if word[0].lower() in vowels:
        return 1 + count_vowels(word[1:])
    return count_vowels(word[1:])
