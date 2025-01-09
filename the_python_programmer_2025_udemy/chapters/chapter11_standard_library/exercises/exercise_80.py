# Exercise 80 - Dataclasses
# Create two dataclasses, Address and Person.
# The Person class should contain a field for storing the person's address, which should be an instance of the Address dataclass.
# The Person class should have the following:
# - name
# - age
# - address (instance of Address)
# - previous_address (list[Address]) [Hint: use default_factory to initialize this list to an empty list if not provided]

# The Address class should have the following:
# - street
# - city
# - zip code

from dataclasses import dataclass, field

@dataclass
class Address:
    street: str
    city: str
    zip_code: str

@dataclass
class Person:
    name: str
    age: int
    address: Address
    previous_address: list[Address] = field (default_factory = list)
