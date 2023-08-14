
class Bean:
    def __init__(self, name, country, max_quantity) -> None:
        self.name = name
        self.country = country
        self.current_quantity = 0
        self.max_quantity = max_quantity

    def add_beans(self, quantity):
        if quantity + self.current_quantity > self.max_quantity:
            raise Exception("Total quantity is exceeding max")
        self.current_quantity += quantity

    def remove_beans(self, quantity):
        self.current_quantity = - quantity
        if self.current_quantity < 0:
            quantity = 0
