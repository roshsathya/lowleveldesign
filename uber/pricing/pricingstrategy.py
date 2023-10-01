from abc import ABC, abstractclassmethod


class PricingStrategy(ABC):

    BASE_FARE = 15  # 15Rps/km

    @abstractclassmethod
    def calculate_price(self, rider_meta_data, trip_meta_data):
        pass


class NightTimePricingStrategy(PricingStrategy):

    @classmethod
    def calculate_price(cls, rider_meta_data, trip_meta_data):
        fare = cls.BASE_FARE + 5
        total_distance = trip_meta_data.destination - trip_meta_data.source
        return total_distance * fare


class SurgePricingStrategy(PricingStrategy):

    @classmethod
    def calculate_price(cls, rider_meta_data, trip_meta_data):
        fare = cls.BASE_FARE + 10
        if rider_meta_data.rating >= 4:
            fare -= 4
        total_distance = trip_meta_data.destination - trip_meta_data.source
        return total_distance * fare


class DefaultPricingStrategy(PricingStrategy):

    @classmethod
    def calculate_price(cls, rider_meta_data, trip_meta_data):
        fare = cls.BASE_FARE
        if rider_meta_data.rating >= 4:
            fare -= 2
        total_distance = trip_meta_data.destination - trip_meta_data.source
        return total_distance * fare
