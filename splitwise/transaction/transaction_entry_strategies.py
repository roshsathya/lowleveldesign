from abc import ABC, abstractmethod
from .transaction import Transaction
from .transaction_group import TransactionGroup


class TransactionEntryStrategies(ABC):

    def __init__(self, user_ids, group_id, total_amount) -> None:
        super().__init__()
        self.user_ids = user_ids
        self.transaction_group = TransactionGroup(
            group_id, total_amount)

    @abstractmethod
    def compute_amount(self, computation, amount):
        pass

    @abstractmethod
    def add_transaction(self, user, amount):
        pass

    def get_transaction_group(self):
        return self.transaction_group


class PaidByUser(TransactionEntryStrategies):
    # Paid by one user and split evenly by everyone

    def __init__(self, user_ids, group_id, total_amount) -> None:
        super().__init__(user_ids, group_id, total_amount)
        self.total_amount = total_amount

    def compute_amount(self, computation, amount):
        return amount

    def add_transaction(self, user, amount=None):
        amount_per_person = self.total_amount / len(self.user_ids)
        primary_user_amount = -1 * (self.total_amount - amount_per_person)
        for user_id in self.user_ids:
            amount = amount_per_person
            if user_id == user.id:
                amount = primary_user_amount
            transaction = Transaction(user, amount=amount)
            self.transaction_group.add_entry(transaction)


class CustomSplit(TransactionEntryStrategies):

    def compute_amount(self, computation, amount):
        return amount

    def add_transaction(self, user, amount):
        transaction = Transaction(user, amount=amount)
        self.transaction_group.add_entry(transaction)


class PercentageSplit(TransactionEntryStrategies):

    # eg. computation = 0.2, amount = 100
    def compute_amount(self, computation, amount):
        return computation * amount

    # Let the percentage be computed before calling the function and passed on as param
    def add_transaction(self, user, amount):
        transaction = Transaction(user, amount=amount)
        self.transaction_group.add_entry(transaction)


class StrategyTypes:

    strategy_dict = {
        "PAID_BY_USER": PaidByUser,
        "CUSTOM_SPLIT": CustomSplit,
        "PERCENTAGE_SPLIT": PercentageSplit
    }
