from pricing.pricingstrategy import NightTimePricingStrategy, \
    SurgePricingStrategy, \
    DefaultPricingStrategy

from driver.driver_strategy import PremiumDriverStrategy, \
    SurgeDriverStrategy, \
    DefaultDriverStrategy


class TripManager:

    manager = None

    def __init__(self) -> None:
        self.trips = {}

    @classmethod
    def get_manager(cls):
        if not cls.manager:
            cls.manager = TripManager()
        return cls.manager

    def get_driver(self, trip_meta_data, rider_meta_data):
        driver_strategy = DefaultDriverStrategy
        if len(self.trips > 50):
            driver_strategy = SurgeDriverStrategy
        elif rider_meta_data.rating >= 4:
            driver_strategy = PremiumDriverStrategy
        drivers = driver_strategy.get_driver()
        if not drivers:
            return None
        return drivers[0]

    def get_price(self, trip_meta_data, rider_meta_data):
        pricing_strategy = DefaultPricingStrategy
        if len(self.trips) > 50:
            pricing_strategy = SurgePricingStrategy
        elif trip_meta_data.created_at > 11 and trip_meta_data.created_at < 5:
            pricing_strategy = NightTimePricingStrategy
        return pricing_strategy.calculate_price(rider_meta_data, trip_meta_data)

    def start_trip(self, trip, rider_meta_data):
        current_price = self.get_price(trip, rider_meta_data)
        driver = self.get_driver(trip, rider_meta_data)
        if not driver:
            print("No drivers found")
            return
        return (driver, current_price)
