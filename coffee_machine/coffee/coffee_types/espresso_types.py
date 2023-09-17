from coffee_machine.coffee.coffee_builder import CoffeeBuilder
from coffee_machine.coffee.constants import *


class FlatWhiteBuilder(CoffeeBuilder):
    system_name = "FLATWHITE"
    name = "Flat White"
    requirements = [MILK, BEANS, SYRUP]
    price = 10

    def __init__(self) -> None:
        super().__init__()
        self.coffee.set_price(self.__class__.price)


class AmericanoBuilder(CoffeeBuilder):
    system_name = "AMERICANO"
    name = "Americano"
    requirements = [WATER, BEANS]
    price = 8

    def __init__(self) -> None:
        super().__init__()
        self.coffee.set_price(self.__class__.price)
