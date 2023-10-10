from abc import abstractclassmethod, ABC
from .driver_manager import DriverManager


class DriverFindingStrategy(ABC):

    BASE_PROXIMITY = 15
    driver_manager = DriverManager.get_manager()

    @abstractclassmethod
    def get_driver(cls):
        pass


class PremiumDriverStrategy(DriverFindingStrategy):

    @classmethod
    def get_driver(cls):
        drivers = [
            driver for driver in cls.driver_manager.drivers if driver.is_available and driver.current_rating >= 4]
        return drivers


class SurgeDriverStrategy(DriverFindingStrategy):

    @classmethod
    def get_driver(cls):
        drivers = [
            driver for driver in cls.driver_manager.drivers if driver.is_available]
        return drivers


class DefaultDriverStrategy(DriverFindingStrategy):

    @classmethod
    def get_driver(cls):
        drivers = [
            driver for driver in cls.driver_manager.drivers if driver.is_available and driver.get_distance() <= cls.BASE_PROXIMITY]
        return drivers
