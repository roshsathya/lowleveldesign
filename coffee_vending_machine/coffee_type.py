
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

    def process_coffee(self):
        pass


class Americano(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "AMERICANO"
        self.base_price = 5

    def process_coffee(self):
        pass


class FlatWhite(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Flat White"
        self.base_price = 5

    def process_coffee(self):
        pass


class Espresso(CoffeeType):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Espresso"
        self.base_price = 5

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
