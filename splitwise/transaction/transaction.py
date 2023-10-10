from datetime import datetime


class Transaction:

    def __init__(self, user_id, amount) -> None:
        self.created_at = datetime.utcnow()
        self.amount = amount
        self.user_id = user_id
