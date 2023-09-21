from .constants import *


class Coffee:

    ingredient_functions = {
        MILK: "add_milk",
        WATER: "add_water",
        BEANS: "add_beans",
        SYRUP: "add_syrup"
    }

    def __init__(self) -> None:
        self.milk = None
        self.water = None
        self.beans = None
        self.syrup = None
        self.price = None
        self.cup = []

    def add_milk(self, milk, quantity):
        self.price += milk.price
        self.cup += (milk, quantity)

    def add_water(self, water, quantity):
        self.price += water.price
        self.cup += (water, quantity)

    def add_beans(self, bean, quantity):
        self.price += bean.price
        self.cup += (bean, quantity)

    def add_syrup(self, syrup, quantity):
        self.price += syrup.price
        self.cup += (syrup, quantity)

    def set_price(self, price):
        self.price = price

    def get_coffee(self):
        return self.cup

    def get_price(self):
        return self.price
