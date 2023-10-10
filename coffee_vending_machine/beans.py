

class Bean:
    def __init__(self, max_quantity) -> None:
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


class ArabicBaean(Bean):
    name = "Arabica"
    country = "Yemen"

    def __init__(self, max_quantity) -> None:
        super().__init__(max_quantity)


class PacasBaean(Bean):
    name = "Arabica"
    country = "Brazil"

    def __init__(self, max_quantity) -> None:
        super().__init__(max_quantity)


class BeanFactory:

    types = {
        1: ArabicBaean,
        2: PacasBaean,
    }

    def __init__(self) -> None:
        pass

    def get_coffee_object(self, bean_type):
        BeanClass = BeanFactory.types.get(bean_type)
        if not BeanClass:
            raise Exception
        return BeanClass()
