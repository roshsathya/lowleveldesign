from snake.snake import Snake
from ladder.ladder import Ladder
from die.die import Die
from user.user import User


class Board:

    def __init__(self, size) -> None:
        self.size = size
        self.die = Die()
        self.grid = [[None for _ in range(self.size)]
                     for _ in range(self.size)]

    def get_obstacles(self, positions, total_obstacles, obstacle_type):
        obstacles = []
        for _ in range(total_obstacles):
            if obstacle_type == "SNAKE":
                obstacle = Snake(self.size)
            elif obstacle_type == "LADDER":
                obstacle = Ladder(self.size)
            if (obstacle.starting_x, obstacle.starting_y) in positions:
                new_position = obstacle.find_new_position(
                    obstacle.starting_x, positions, self.size)
                obstacle.starting_x = new_position[0]
                obstacle.starting_y = new_position[1]

            if (obstacle.ending_x, obstacle.ending_y) in positions:
                new_position = obstacle.find_new_position(
                    obstacle.ending_x, positions, self.size)
                obstacle.ending_x = new_position[0]
                obstacle.ending_y = new_position[1]

            obstacles.append(obstacle)
        return obstacles

    def build_board(self, total_snakes: int = 0, total_ladders: int = 0):
        if not total_snakes:
            total_snakes = self.size
        if not total_ladders:
            total_ladders = self.size

        positions = set()
        snakes = self.get_obstacles(positions, total_snakes, "SNAKE")
        ladders = self.get_obstacles(positions, total_ladders, "LADDER")

        for obstacle in snakes + ladders:
            self.grid[obstacle.starting_x][obstacle.starting_y]

    def roll_die(self, user: User):
        steps = self.die.roll()
        if user.current_x % 2 == 0:
            user.current_y += steps
            if user.current_y >= self.size:
                user.current_x += 1
                user.current_y = self.size - 1 - (user.current_y % self.size)
        else:
            user.current_y -= steps
            if user.current_y < 0:
                user.current_x += 1
                user.current_y = user.current_y % self.size

        if user.current_x >= self.size or user.current_x == self.size - 1 and user.current_y == self.size - 1:
            return True

        obstacle = self.grid[user.current_x][user.current_y]
        if obstacle:
            user.current_x = obstacle.ending_x
            user.current_y = obstacle.ending_y

        return False
