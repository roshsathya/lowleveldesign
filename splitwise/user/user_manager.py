from .user import User


class UserManager:

    manager = None

    @classmethod
    def get_manager(cls):
        if not cls.manager:
            cls.manager = UserManager()
        return cls.manager

    def __init__(self) -> None:
        self.users = {}

    def get_user(self, email_address):
        return self.users.get(email_address)

    def register_user(self, name, email_address):
        self.users[email_address] = User(name, email_address)
        return self.users[email_address]
