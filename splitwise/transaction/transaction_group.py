from datetime import datetime


class TransactionGroup:
    def __init__(self, group_id, total_amount) -> None:
        self.created_on = datetime.utcnow()
        self.id = str(hash(group_id + str(self.created_on)))
        self.group_id = group_id
        self.transactions = {}
        self.total_amount = total_amount
        self.current_amount = 0

    def add_entry(self, transaction):
        if transaction.user_id in self.transactions:
            self.current_amount -= self.transactions[transaction.user_id].amount
        if transaction.amount > (self.total_amount - self.current_amount):
            return
        self.current_amount += transaction.amount
        self.transactions[transaction.user_id] = transaction

    def verify_group(self):
        return self.current_amount == self.total_amount
