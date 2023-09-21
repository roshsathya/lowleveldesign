from coffee.coffee_factory import CoffeeFactory
from coffee.coffee import Coffee
from coffee.constants import *


class CoffeeManager:
    def __init__(self, total_bean_disp, total_water_disp, total_milk_disp, total_syrup_disp) -> None:
        self.bean_dispensers = {}
        self.water_dispensers = {}
        self.milk_dispensers = {}
        self.syrup_dispensers = {}
        self.total_bean_disp = total_bean_disp
        self.total_water_disp = total_water_disp
        self.total_milk_disp = total_milk_disp
        self.total_syrup_disp = total_syrup_disp
        self.coffee = None

    def add_bean(self, bean_dispenser):
        if self.total_bean_disp == 0:
            return
        self.total_bean_disp -= 1
        item = bean_dispenser.get_item()
        self.bean_dispensers[item.system_name] = bean_dispenser

    def add_water(self, water_dispenser):
        if self.total_water_disp == 0:
            return
        self.total_water_disp -= 1
        item = water_dispenser.get_item()
        self.water_dispensers[item.system_name] = water_dispenser

    def add_milk(self, milk_dispenser):
        if self.total_milk_disp == 0:
            return
        self.total_milk_disp -= 1
        item = milk_dispenser.get_item()
        self.milk_dispensers[item.system_name] = milk_dispenser

    def add_syrup(self, syrup_dispenser):
        if self.total_syrup_disp == 0:
            return
        self.total_syrup_disp -= 1
        item = syrup_dispenser.get_item()
        self.syrup_dispensers[item.system_name] = syrup_dispenser

    def get_available_beans(self):
        return [dispenser.item.name for dispenser in self.bean_dispensers.values()
                if dispenser.quantity]

    def get_available_waters(self):
        return [dispenser.item.name for dispenser in self.water_dispensers.values()
                if dispenser.quantity]

    def get_available_milks(self):
        return [dispenser.item.name for dispenser in self.milk_dispensers.items()
                if dispenser.quantity]

    def get_coffee_category(self):
        return [category.name for category in CoffeeFactory.categories.values()]

    def get_coffee_types(self, coffee_category):
        return [coffee.name for coffee in CoffeeFactory.categories[coffee_category].all_types]

    def select_coffee_type(self, coffee_type):
        self.coffee = CoffeeFactory.get_coffee(
            self.coffee_category, coffee_type)

    def set_coffee_beans(self, bean):
        if not self.coffee:
            return
        func = Coffee.ingredient_functions[BEANS]
        setattr(self.coffee, func, bean)

    def get_coffee_requirements(self):
        if not self.coffee:
            return
        funcs_dict = {
            BEANS: self.set_coffee_beans
        }
        requirement_funcs = []
        for requirement in self.coffee.requirements:
            requirement_funcs.append(funcs_dict[requirement])
        return requirement_funcs

    def build_coffee(self):
        return self.coffee.cup

    def get_coffee_price(self):
        return self.coffee.price
