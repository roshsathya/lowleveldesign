

class CoffeeTemp:
    def __init__(self) -> None:
        self.cost = None


class HotCoffee(CoffeeTemp):
    def __init__(self, cost) -> None:
        super().__init__()
        self.key = 1
        self.cost = cost


class ColdCoffee(CoffeeTemp):
    def __init__(self, cost) -> None:
        super().__init__()
        self.key = 2
        self.cost = cost


class CoffeeType:

    def __init__(self) -> None:
        self.name = None
        self.coffee_temp = {}

    def process_coffee(self):
        raise Exception("process coffee function should be implemented")


class Cappuccino(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "CAPPUCCINO"
        self.base_price = 10
        self.coffee_temp['HOT'] = HotCoffee(self.base_price + 5)

    def process_coffee(self):
        pass


class Americano(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "AMERICANO"
        self.base_price = 5
        self.coffee_temp['HOT'] = HotCoffee(self.base_price + 5)
        self.coffee_temp['COLD'] = ColdCoffee(self.base_price + 2)

    def process_coffee(self):
        pass


class FlatWhite(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Flat White"
        self.base_price = 5
        self.coffee_temp['HOT'] = HotCoffee(self.base_price + 5)

    def process_coffee(self):
        pass


class Espresso(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Espresso"
        self.base_price = 5
        self.coffee_temp['HOT'] = HotCoffee(self.base_price + 5)

    def process_coffee(self):
        pass


class CoffeeProcessingFactory:

    coffee_types = {
        1: Cappuccino,
        2: Espresso,
        3: FlatWhite,
        4: Americano
    }

    def __init__(self) -> None:
        pass

    def get_coffee_object(self, coffee_type):
        CoffeeClass = CoffeeProcessingFactory.coffee_types.get(coffee_type)
        if not CoffeeClass:
            raise Exception
        return CoffeeClass()
