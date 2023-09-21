from coffee_machine.coffee.coffee_builder import CoffeeBuilder
from coffee_machine.coffee.constants import *


class JavaChipBuilder(CoffeeBuilder):
    system_name = "JAVACHIP"
    name = "Java Chip"
    requirements = [MILK, BEANS, SYRUP]
    price = 15

    def __init__(self) -> None:
        super().__init__()
        self.coffee.set_price(self.__class__.price)


class MochaBuilder(CoffeeBuilder):
    system_name = "MOCHA"
    name = "Mocha"
    requirements = [MILK, BEANS]
    price = 12

    def __init__(self) -> None:
        super().__init__()
        self.coffee.set_price(self.__class__.price)
