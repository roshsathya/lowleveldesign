
class Milk():
    def __init__(self) -> None:
        super().__init__()
        self.expiry_on = None

    def set_expiry_on(self, expiry_on_date):
        self.expiry_on = expiry_on_date
