# Exercise 75 - Banking System [Part 2/2]
# So far we've defined the `Card` and `Account` classes. Now, let's define the `BankCustomer` class.


# The `BankCustomer` class should also have the following methods:
# 1. add_account(self, account: Account) -> None: adds an account to the accounts list.
# 2. remove_account(self, account_number: int) -> None: removes an account from the accounts list.
# 3. add_card(self, card: Card) -> None: adds a card to the cards list.
# 4. remove_card(self, card_number: int) -> None: removes a card from the cards list.
# 3. get_account(self, account_number: int) -> Account: returns an account based on the account number.
# 4. get_card(self, card_number: int) -> Card: returns a card based on the card number.
# 5. get_total_balance(self) -> float: returns the total balance of all accounts.
# 6. withdraw(self, account_number: int, amount: float, card_number: int, pin: int) -> None: withdraws money from an account.
# 7. deposit(self, account_number: int, amount: float) -> None: deposits money into an account.

# See `test_e75()` in `tests/test_ch10.py` for the expected behavior.

from .exercise_74 import Account, Card, Customer

class BankCustomer(Customer):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.accounts: list[Account] = []
        self.cards: list[Card] = []
        self.total_balance: float = 0.0

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)
        self.cards.extend(account.cards)
        self.total_balance += account.balance

    def remove_account(self, account_number: str) -> None:
        account = self.get_account(account_number)
        for card in account.cards:
            self.cards.remove(card)
        self.total_balance -= account.balance
        self.accounts.remove(account)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_number: str) -> None: ...

    def get_account(self, account_number: str) -> Account:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise ValueError(f"Account with number {account_number} not found")

    def get_card(self, card_number: str) -> Card:
        for card in self.cards:
            if card.card_number == card_number:
                return card
        raise ValueError(f"Card with number {card_number} not found")

    def get_total_balance(self) -> float:
        return self.total_balance

    def withdraw(
        self, account_number: str, amount: float, card_number: str, pin: str
    ) -> None:
        account = self.get_account(account_number)
        card = self.get_card(card_number)
        if card.pin != pin:
            raise ValueError("Invalid pin")
        if account.balance < amount:
            raise ValueError("Insufficient funds")
        account.balance -= amount
        self.total_balance -= amount

    def deposit(self, account_number: str, amount: float) -> None:
        try:
            account = self.get_account(account_number)
            account.balance += amount
            self.total_balance += amount
        except ValueError as e:
            print(f"Error: Cannot deposit with unknown account number {account_number}")
