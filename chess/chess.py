class ImpossibleSettle(Exception):
    pass


class Board():

    X_AXIS = frozenset(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'))
    Y_AXIS = frozenset(('1', '2', '3', '4', '5', '6', '7', '8'))

    def __init__(self):
        self.squares = {x: {y: None for y in self.Y_AXIS} for x in self.X_AXIS}

    def settle(self, rook, x, y):
        if x not in self.X_AXIS or y not in self.Y_AXIS or self.squares[x][y] is not None:
            raise ImpossibleSettle

        self.squares[x][y] = rook


class Rook():
    pass
