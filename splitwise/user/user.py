from datetime import datetime
from group.group import Group


class User:
    def __init__(self, name, email_address) -> None:
        self.created_on = datetime.utcnow()
        self.user_id = str(hash(f"{name}{self.created_on}"))
        self.name = name
        self.email_address = email_address
        self.image = None
        self.groups = {}

    def add_image(self, image):
        self.image = image

    def create_group(self, group_name):
        group = Group(group_name)
        group_id = group.get_group_id()
        self.groups[group_id] = group
        return group

    def compute_total_dues(self):
        total = 0
        for group in list(self.groups.values()):
            user = group.get_user(self.user_id)
            total += user.total_amount
        return total
