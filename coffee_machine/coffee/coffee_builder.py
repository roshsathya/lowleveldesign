from .coffee import Coffee


class CoffeeBuilder():
    def __init__(self) -> None:
        super().__init__()
        self.coffee = Coffee()

    def add_milk(self, milk_type, quantity):
        self.coffee.add_milk(milk_type, quantity)

    def add_water(self, water_type, quantity):
        self.coffee.add_milk(water_type, quantity)

    def add_beans(self, bean_type, quantity):
        self.coffee.add_milk(bean_type, quantity)

    def add_syrup(self, syrup_type, quantity):
        self.coffee.add_milk(syrup_type, quantity)

    def set_price(self, price):
        self.coffee.set_price(price)
