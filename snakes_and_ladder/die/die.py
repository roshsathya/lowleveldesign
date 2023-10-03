from random import randint


class Die:

    def __init__(self) -> None:
        pass

    def roll(self):
        return randint(1, 6)
