class Dispenser:
    def __init__(self, item, max_quantity) -> None:
        self.item = item
        self.max_quantity = max_quantity
        self.current_quantity = 0
        self.last_serviced = None

    def get_dispenser_item(self):
        return self.item

    def get_dispenser_quantity(self):
        return self.current_quantity

    def add_item(self, quantity):
        if quantity + self.current_quantity > self.max_quantity:
            return
        self.current_quantity += quantity

    def remove_item(self, quantity):
        if self.current_quantity == 0:
            return
        self.current_quantity -= quantity
        return (self.item, quantity)
