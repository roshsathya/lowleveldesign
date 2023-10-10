

class RiderManager:

    manager = None

    def __init__(self) -> None:
        self.riders = {}

    @classmethod
    def get_manager(cls):
        if not cls.manager:
            cls.manager = RiderManager()
        return cls.manager

    def register(self, rider):
        self.riders[rider.id] = rider
