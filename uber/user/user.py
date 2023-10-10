from datetime import datetime
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.id = str(hash(name + str(datetime.utcnow())))
        self.current_location = None
        self.trip = None

    @abstractmethod
    def register_user(self):
        pass

    @abstractmethod
    def get_meta_data(self):
        pass

    def assign_trip(self, trip):
        self.trip = trip

    @abstractmethod
    def cancel_trip(self):
        pass
