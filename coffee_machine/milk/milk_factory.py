from .milk_types import *


class MilkFactory:
    milk_types = {
        Almond.system_name: Almond,
        FullCream.system_name: FullCream,
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def get_milk(cls, milk_type):
        MilkClass = cls.milk_types.get(milk_type)
        if not MilkClass:
            raise Exception
        return MilkClass()
