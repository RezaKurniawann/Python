# Exercise 67 - Exception Group
# Given the following function, we want to raise an exception called `ExceptionGroup` if multiple errors occur during processing.
# Fix this function so that it appends the exceptions to a list and raises an `ExceptionGroup` if multiple errors occur.

def process_strings(strings: list[str]):
    exceptions = []
 
    for string in strings:
        try:
            # Operation 1: Convert to Integer
            print(f"Converting '{string}' to integer: {int(string)}")
 
            # Operation 2: Access First Character
            print(f"First character of '{string}' is '{string[1]}'")
 
        except ValueError:
            exceptions.append(ValueError("Could not convert the string to an integer"))
 
        except IndexError:
            exceptions.append(IndexError("Could not access the first character"))
 
    if exceptions:
        raise ExceptionGroup("Multiple errors occurred during processing", exceptions)
