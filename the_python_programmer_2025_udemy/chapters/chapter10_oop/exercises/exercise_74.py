# Exercise 74 - Banking System [Part 1/2]
# In the next three exercises, you will implement a simple banking system.
# Let's start first by defining our core classes (Card, Account, and Customer).

# Create three dataclasses called `Card`, `Account`, and `Customer`.

# The `Card` class should have the following attributes:
# 1. card_number (a string)
# 2. card_holder (a string)
# 3. expiration_date (a string)
# 4. pin (a string)

# The `Account` class should have the following attributes:
# 1. account_number (a string)
# 2. account_holder (an instance of the `Customer` class)
# 3. balance (a float)
# 4. cards (a list of `Card` instances)

# The `Customer` class should have the following attributes:
# 1. first_name (a string)
# 2. last_name (a string)
# 3. accounts (a list of `Account` instances)
# 4. cards (a list of `Card` instances)
# 5. total_balance (a float)

# See `test_e74()` in `tests/test_ch10.py` for the expected behavior.

from __future__ import annotations
from dataclasses import dataclass, field  # noqa: F401


@dataclass
class Card:
    card_number: str
    card_holder: str
    account_number: str
    expiration_date: str
    pin: str

@dataclass
class Account:
    account_number: str
    account_holder: str
    balance: float
    cards: list[Card] = field (default_factory = list)
    
    def add_card (self, card: Card):
        self.cards.append(card)
    
    def remove_card (self, card: Card):
        self.cards.remove(card)

@dataclass
class Customer:
    first_name: str
    last_name: str
    accounts: list[Account] = field (default_factory = list)
    cards: list[Card] = field (default_factory = list)
    total_balance: float = 0.0


