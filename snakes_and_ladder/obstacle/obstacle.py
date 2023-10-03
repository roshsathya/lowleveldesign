from random import randint


class Obstacle:

    def find_new_position(cls, row, positions, grid_size):
        while True:
            new_position = (row, randint(0, grid_size-1))
            if new_position in positions:
                continue
            return new_position
