from datetime import datetime
from transaction.transaction_entry_strategies import StrategyTypes, PaidByUser
from user.user_manager import UserManager


class GroupUser:

    def __init__(self, user) -> None:
        self.user_id = user.id
        self.name = user.name
        self.image = user.image
        self.total_amount = 0

    def update_dues(self, amount):
        self.total_amount += amount


class Group:
    def __init__(self, name) -> None:
        self.name = name
        self.id = str(hash(f"{name} {str(datetime.utcnow())}"))
        self.image = None
        self.transactions_groups = {}
        self.checkpoints = []
        self.users = {}

    def get_group_id(self):
        return self.id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def upload_image(self, image):
        self.image = image

    def add_user(self, email_address):
        manager = UserManager.get_manager()
        user = manager.users.get(email_address)
        if not user:
            print("User is not registered")
            return
        self.users[user.id] = GroupUser(user)

    def initiate_transaction(self, transaction_type, total_amount):
        TransactionStrategy = StrategyTypes.strategy_dict.get(transaction_type)
        transaction_group = TransactionStrategy.get_transaction_group()
        self.transactions_groups[transaction_group.id] = transaction_group
        return TransactionStrategy(self.id, total_amount)

    def set_transaction(self, transaction_group_id):
        for transaction in self.transactions_groups.get(transaction_group_id, []):
            user = self.users.get(transaction.user_id)
            user.update_dues(transaction.amount)

    def settle_payment(self, sender_user_id, reciever_user_id, amount=None):
        if not amount:
            amount = 0
            for trans_group in list(self.transactions_groups.values()):
                sender_transaction = trans_group.transactions.get(
                    sender_user_id)
                reciever_transaction = trans_group.transactions.get(
                    reciever_user_id)
                if sender_transaction and reciever_transaction and reciever_transaction.amount < 0 and sender_transaction > 0:
                    amount += sender_transaction.amount

        transaction = PaidByUser(
            [sender_user_id, reciever_user_id], self.id, amount)

        transaction_group = transaction.get_transaction_group()
        self.transactions_groups[transaction_group.id] = transaction_group
        self.set_transaction(transaction_group.id)
