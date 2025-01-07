# Exercise 40 - Anagrams
# Write a funtion that takes two strings and check if they are anagrams.
# An Anagram is a word formed by rearranging the letters of a different word, using all the original letters exactly once.
# For example, the words "listen" and "silent" are anagrams.

# Assume that the input strings are lowercase and contain only letters.
def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)
 
# Or using Counter from `collections` module
from collections import Counter
 
def is_anagram(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)
    
