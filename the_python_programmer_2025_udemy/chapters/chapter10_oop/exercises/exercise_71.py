# Exercise 71 - Library Management System [Part 1/3]
# In the next three exercises, you will implement a simple library management system.
# Let's start first by defining our core classes (Book and Author).

# Create two dataclasses called `Author` and `Book` and an enum called `Genre`.
# The `Author` class should have the following attributes:
# 1. first_name
# 2. last_name

# The `Book` class should have the following attributes:
# 1. title
# 2. author (an instance of the `Author` class)
# 3. publication_year
# 4. genre (an instance of the `Genre` enum)

# The `Genre` enum should have the following values:
# 1. Fiction
# 2. NonFiction
# 3. Biography
# 4. History
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

 
class Genre(Enum):
    Fiction = 1
    NonFiction = 2
    Biography = 3
    History = 4
 
 
@dataclass
class Author:
    first_name: str
    last_name: str
 
    def __hash__(self):
        return hash((self.first_name, self.last_name))
 
 
@dataclass
class Book:
    title: str
    author: Author
    publication_year: int
    genre: Genre
 
    def __hash__(self):
        return hash((self.title, self.author, self.publication_year, self.genre))
 
    def __eq__(self, other: Book):
        return (
            self.title == other.title
            and self.author == other.author
            and self.publication_year == other.publication_year
            and self.genre == other.genre
        )
