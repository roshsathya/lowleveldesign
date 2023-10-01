from user.user import User
from .rider_manager import RiderManager
from trip.trip import Trip


class Rider(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.is_premium_user = False
        self.total_rides = 0
        self.current_rating = 0
        self.rider_manager = RiderManager.get_manager()

    def get_meta_data(self):
        return {
            'is_premium_user': self.is_premium_user,
            'total_rides': self.total_rides,
            'current_rating': self.current_rating,
            'id': self.id
        }

    def register_user(self):
        self.rider_manager.register(self)

    def initiate_trip(self, source, destination):
        rider_meta_data = self.get_meta_data()
        return Trip(rider_meta_data, source, destination)

    def start_trip(self, trip):
        rider_meta_data = self.get_meta_data()
        trip.start_strip(rider_meta_data)

    def cancel_trip(self):
        if not self.trip:
            return
        self.trip.cancel_trip("RIDER")
