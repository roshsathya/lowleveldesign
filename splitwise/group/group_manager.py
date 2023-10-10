class GroupManager:

    manager = None

    @classmethod
    def get_manager(cls):
        if not cls.manager:
            cls.manager = GroupManager()
        return cls.manager

    def __init__(self) -> None:
        self.groups = {}

    def register_group(self, group):
        self.groups[group.id] = group
