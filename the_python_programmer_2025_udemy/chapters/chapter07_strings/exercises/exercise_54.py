# Exercise 54 - Extract Error Messages
# You are given a list of log entries from a server. Each entry is a string that contains:
# a log level, and a message, separated by spaces.

# Write a function that takes this list of log entries and returns a list of error messages
# which are associated with the log level "ERROR".

# For example, given the following list of log entries:
# log_entries = [
#     "INFO User logged in",
#     "ERROR Unable to connect to the server",
#     "ERROR Server error",
#     ]
# The function should return ["Unable to connect to the server", "Server error"].

def extract_error_messages(log_entries: list[str]) -> list[str]:
    errors = []
    for entry in log_entries:
        if entry.startswith("ERROR"):
            errors.append(entry.split(" ", 1)[1])
    return errors
 
 
# Or using list comprehension
def extract_error_messages(log_entries: list[str]) -> list[str]:
    return [
        entry.split(" ", 1)[1] for entry in log_entries if entry.startswith("ERROR")
    ]
