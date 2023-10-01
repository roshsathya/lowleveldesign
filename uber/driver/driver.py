from user.user import User


class Driver(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.is_available = False
        self.total_distance = 0
        self.total_rides = 0
        self.current_rating = 0
        self.user_reviews = []

    def get_distance(self, rider_metadata):
        # Need to use self.current_location and the riders_location to calculate
        return 7

    def get_meta_data(self):
        return {
            'name': self.name,
            'total_ride': self.total_rides,
            'current_rating': self.current_rating,
            'id': self.id,
            'user_reviews': self.user_reviews
        }

    def cancel_trip(self):
        if not self.trip:
            return
        self.trip.cancel_trip("DRIVER")
