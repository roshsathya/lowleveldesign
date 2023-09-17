from .coffee_types.espresso_types import *
from .coffee_types.frappuccino_types import *


class FrappuccinoFactory:
    name = "Frappuccino"
    all_types = {
        JavaChipBuilder.system_name:  JavaChipBuilder,
        MochaBuilder.system_name: MochaBuilder
    }

    @classmethod
    def get_coffee(cls, coffee_type):

        if coffee_type not in cls.all_types:
            return
        return cls.all_types.get(coffee_type)


class EspressoFactory:
    name = 'Espresso'
    all_types = {
        FlatWhiteBuilder.system_name:  FlatWhiteBuilder,
        AmericanoBuilder.system_name: AmericanoBuilder
    }

    @classmethod
    def get_coffee(cls, coffee_type):

        if coffee_type not in cls.all_types:
            return
        return cls.all_types.get(coffee_type)


class CoffeeFactory:
    categories = {
        "FRAPPUCCINO": FrappuccinoFactory,
        "ESPRESSO": EspressoFactory
    }

    @classmethod
    def get_coffee(cls, category, coffee_type):

        if category not in cls.categories:
            return
        return cls.categories[category][coffee_type]
