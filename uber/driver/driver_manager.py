
class DriverManager:

    manager = None

    def __init__(self) -> None:
        self.drivers = {}

    def get_manager(cls):
        if not cls.manager:
            cls.manager = DriverManager()
        return cls.manager
