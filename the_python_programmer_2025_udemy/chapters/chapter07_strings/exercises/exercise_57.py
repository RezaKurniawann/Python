# Exercise 57 - String Compression
# Write a function that compresses a string using a simple compression algorithm.
# If a character appears more than once in a row, replace the sequence with
# the character followed by the number of times it appears.
# For example, the string "aaabbbbbcc" would be compressed to "a3b5c2".

def compress_string(s: str) -> str:
    if not s:  # if s is an empty string
        return ""
    compressed = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        elif count == 1:
            compressed += s[i - 1]
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    compressed += s[-1] + str(count) if count > 1 else s[-1]  # Using a ternary operator
    return compressed

