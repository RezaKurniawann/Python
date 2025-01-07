# Exercise 46 - Valid Parentheses
# Write a function that takes a string containing only parentheses '(', ')', '{', '}', '[' and ']'
# and returns True if the parentheses are valid, and False otherwise.
# For example, the string "([])" should return True, and the string "())" should return False.


def valid_parentheses(parentheses: str) -> bool:
    matching = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in parentheses:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():  
            if not stack or stack[-1] != matching[char]:  
                return False
            stack.pop()  

    return not stack  

def valid_parentheses(parentheses: str) -> bool:
    stack = []
    for char in parentheses:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return not stack
