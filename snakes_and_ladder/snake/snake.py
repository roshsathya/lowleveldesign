from random import randint
from obstacle.obstacle import Obstacle


class Snake(Obstacle):

    def __init__(self, grid_size) -> None:
        self.starting_x = randint(1, grid_size-1)
        self.starting_y = randint(0, grid_size-1)
        self.ending_x = randint(0, self.starting_x-1)
        self.ending_y = randint(0, grid_size-1)
