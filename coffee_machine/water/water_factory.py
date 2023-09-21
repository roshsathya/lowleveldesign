from .water_types import *


class WaterFactory:
    water_types = {
        Still.system_name: Still,
        Sparkling.system_name: Sparkling,
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def get_water(cls, water_type):
        WaterClass = cls.water_types.get(water_type)
        if not WaterClass:
            raise Exception
        return WaterClass()
