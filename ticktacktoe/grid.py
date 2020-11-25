import numpy


class Grid:
    N = 0
    field = []
    player_wins = []
    computer_wins = []

    def __init__(self, n=3):
        self.N = n
        self.field = numpy.zeros([self.N, self.N])
        self.player_wins = numpy.ones(self.N)
        self.computer_wins = numpy.full(self.N, -1)

    def mark(self, i, j, mark=1):
        self.field[i, j] = mark

    def check(self):
        for i in range(self.N):
            if numpy.all(self.field[i] == self.player_wins):
                return 1
            if numpy.all(self.field.T[i] == self.player_wins):
                return 1
            if numpy.all(numpy.diagonal(self.field) == self.player_wins):
                return 1
            if numpy.all(numpy.diagonal(self.field[::-1]) == self.player_wins):
                return 1
            if numpy.all(self.field[i] == self.computer_wins):
                return -1
            if numpy.all(self.field.T[i] == self.computer_wins):
                return -1
            if numpy.all(numpy.diagonal(self.field) == self.computer_wins):
                return -1
            if numpy.all(numpy.diagonal(self.field[::-1]) == self.computer_wins):
                return -1
        return 0
