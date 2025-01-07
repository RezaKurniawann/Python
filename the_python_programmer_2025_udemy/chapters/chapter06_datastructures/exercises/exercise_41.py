# Exercise 41 - Remove Duplicates
# Write a function that takes a list of integers and returns a new list with duplicates removed.
# For example, the list [1, 2, 2, 3, 3, 3] should return [1, 2, 3].


def remove_duplicates(my_list: list[int]) -> list[int]:
    result = []
    for number in my_list:
        if number not in result:
            result.append(number)
    return result
 

def remove_duplicates(my_list: list[int]) -> list[int]:
    return list(set(my_list))
