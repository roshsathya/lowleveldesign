
class CoffeeTemp:
    def __init__(self) -> None:
        pass

    def compute_cost(self):
        raise Exception()


class HotCoffee(CoffeeTemp):
    def __init__(self) -> None:
        super().__init__()
        self.key = 1
        self.base_price = 5


class ColdCoffee(CoffeeTemp):
    def __init__(self) -> None:
        super().__init__()
        self.key = 2
        self.base_price = 10


class CoffeeTempFactory:

    types = {
        1: HotCoffee,
        2: ColdCoffee,
    }

    def __init__(self) -> None:
        pass

    def get_coffee_object(self, type):
        TempClass = CoffeeTempFactory.types.get(type)
        if not TempClass:
            raise Exception
        return TempClass()
