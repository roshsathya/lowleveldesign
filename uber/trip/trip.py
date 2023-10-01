from datetime import datetime
from .trip_manager import TripManager


class TripStatus:
    INITIATED = "INITIATED"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"
    CANCELLED_BY_RIDER = "CANCELLED_BY_RIDER"
    CANCELLED_BY_DRIVER = "CANCELLED_BY_DRIVER"


class Trip:
    def __init__(self, rider, source, destination) -> None:
        self.created_on = datetime.utcnow()
        self.status = TripStatus.INITIATED
        self.source = source
        self.destination = destination
        self.rider = rider
        self.assigned_driver = None
        self.trip_fare = None
        self.trip_manager = TripManager.get_manager()

    def calculate_distance(self):
        return self.destination - self.source

    def get_trip_meta_data(self) -> {"source": int, "destination": int, "created_on": type(datetime)}:
        return {
            'source': self.source,
            'destination': self.destination,
            "created_at": self.created_on
        }

    def get_price(self, rider_meta_data):
        trip_meta_data = self.get_trip_meta_data()
        return self.trip_manager.get_price(trip_meta_data, rider_meta_data)

    def start_trip(self, rider_meta_data):
        self.assign_driver, self.trip_fare = self.trip_manager.start_trip(
            rider_meta_data)

        self.rider.assign_trip(self)
        self.driver.assign_trip(self)
        self.status = TripStatus.ONGOING

    def cancel_trip(self, source):
        if source == "RIDER":
            self.status = TripStatus.CANCELLED_BY_RIDER
        if source == "DRIVER":
            self.status = TripStatus.CANCELLED_BY_DRIVER
