# Exercise 79 - Calculate Days Until Next Birthday
# Given a birthday represented as a date object,
# write a function that calculates the number of days until the next birthday.

from datetime import date


def days_until_next_birthday(birthday: date, now: date = date.today()) -> int:
    current_year_birthday = date(now.year, birthday.month, birthday.day)

    if now <= current_year_birthday:
        return (current_year_birthday - now).days

    next_year_birthday = date (now.year + 1, birthday.month, birthday.day)
    return (next_year_birthday - now).days
