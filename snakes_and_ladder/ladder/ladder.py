from random import randint


class Ladder:

    def __init__(self, grid_size) -> None:
        self.starting_x = randint(0, grid_size-2)
        self.starting_y = randint(0, grid_size-1)
        self.ending_x = randint(self.starting_x+1, grid_size-1)
        self.ending_y = randint(0, grid_size-1)
