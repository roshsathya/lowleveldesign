from coffee_manager import CoffeeManager
from dispenser import Dispenser
from beans.beans_factory import BeansFactory
from beans.constants import *
from water.water_factory import WaterFactory
from water.constants import *
from milk.milk_factory import MilkFactory
from milk.constants import *
from syrup.syrup_factory import SyrupFactory
from syrup.constants import *


class UIInterface:
    def __init__(self) -> None:
        self.coffee_category = None
        self.coffee_type = None
        self.coffee_manager = self.initialise_machine()

    def initialise_machine(self):
        coffee_manager = CoffeeManager(
            total_bean_disp=3, total_water_disp=2, total_milk_disp=2)

        # Adding beans into dispensers
        arabica_obj = BeansFactory.get_bean(ARABICA)
        arabica_bean_dispenser = Dispenser(arabica_obj, 100)
        coffee_manager.add_bean(arabica_bean_dispenser)

        robusta_obj = BeansFactory.get_bean(ROBUSTA)
        robusta_bean_dispenser = Dispenser(robusta_obj, 100)
        coffee_manager.add_bean(robusta_bean_dispenser)

        liberica_obj = BeansFactory.get_bean(LIBERICA)
        liberica_bean_dispenser = Dispenser(liberica_obj, 100)
        coffee_manager.add_bean(liberica_bean_dispenser)

        # Adding water into dispensers
        still_water_obj = WaterFactory.get_bean(STILL)
        still_water_dispenser = Dispenser(still_water_obj, 100)
        coffee_manager.add_water(still_water_dispenser)

        sparkling_obj = WaterFactory.get_bean(SPARKLING)
        sparkling_dispenser = Dispenser(sparkling_obj, 100)
        coffee_manager.add_water(sparkling_dispenser)

        # Adding milk into dispensers
        almond_obj = MilkFactory.get_bean(ALMOND)
        almond_dispenser = Dispenser(almond_obj, 100)
        coffee_manager.add_milk(almond_dispenser)

        full_cream_obj = MilkFactory.get_bean(FULLCREAM)
        full_cream_dispenser = Dispenser(full_cream_obj, 100)
        coffee_manager.add_milk(full_cream_dispenser)

        # Adding syrup into dispensers
        vanilla_obj = SyrupFactory.get_bean(VANILLA)
        vanilla_dispenser = Dispenser(vanilla_obj, 100)
        coffee_manager.add_syrup(vanilla_dispenser)

        strawberry_obj = SyrupFactory.get_bean(STRAWBERRY)
        strawberry_dispenser = Dispenser(strawberry_obj, 100)
        coffee_manager.add_syrup(strawberry_dispenser)

        return coffee_manager

    def get_coffee_category(self):
        return self.coffee_manager.get_coffee_category

    def select_coffee_category(self, coffee_category):
        self.coffee_category = coffee_category
        return self.get_coffee_types(coffee_category)

    def get_coffee_types(self, coffee_category):
        return self.coffee_manager.get_coffee_types(coffee_category)

    def select_coffee_type(self, coffee_type):
        self.coffee_manager.select_coffee_type(coffee_type)

    def get_requirements(self):
        return self.coffee_manager.get_requirements()

    def build_coffee(self):
        self.coffee_manager.build_coffee()
