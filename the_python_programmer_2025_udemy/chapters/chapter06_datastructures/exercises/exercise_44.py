# Exercise 44 - Sum of Frequency Tuples
# Write a function that takes a list of tuples where each tuple
# contains a name (string) and a frequency (integer) and returns a dictionary that
# contains the sum of the frequencies for each name.
# For example, the list [('a', 1), ('b', 2), ('a', 3)] should return {'a': 4, 'b': 2}.

def sum_of_freq_tuples(lst: list[tuple[str, int]]) -> dict[str, int]:
    freq_dict = {}
    
    for name, freq in lst:
        if name in freq_dict:
            freq_dict[name] += freq
        else:
            freq_dict[name] = freq
    
    return freq_dict

def sum_of_freq_tuples(lst: list[tuple[str, int]]) -> dict[str, int]:
    result = {}
    for name, freq in lst:
        result[name] = result.get(name, 0) + freq
    return result
