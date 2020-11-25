import numpy
import random


class GameStrategyInterface:

    def choose_cell(self, grid):
        raise NotImplemented


class RandomGameStrategy(GameStrategyInterface):

    def choose_cell(self, grid):
        i = random.randint(0, grid.N - 1)
        j = random.randint(0, grid.N - 1)
        k = grid.N * grid.N
        while grid.field[i, j] != 0 and k > 0:
            k -= 1
            i = random.randint(0, grid.N - 1)
            j = random.randint(0, grid.N - 1)
        if k > 0:
            return i, j
        else:
            return None, None


class AI:
    game_strategy = None

    def __init__(self):
        self.game_strategy = RandomGameStrategy()

    def mark_cell(self, grid):
        return self.game_strategy.choose_cell(grid)
