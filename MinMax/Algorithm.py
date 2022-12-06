import random
import MiniMax as nx


class Algorithm:

    def __init__(self, board, level, humanPiece, iaPiece):
        self.board = board
        self.human = humanPiece
        self.ia = iaPiece
        self.setLevel(level)

    def setLevel(self, level):
        self.level = level
        """
        RANDOM = 0
        3 PROFUNDIDAD = 1
        5 PROFUNDIDAD = 2
        MINIMAX = 3
        """

    def getValue(self):
        if self.level == 0:
            valid = False
            val = 0
            while not valid:
                val = random.randint(1, 9)
                if self.board.isValid(val):
                    valid = True
            return val
        else:
            return nx.MiniMax(self.board, self.ia, self.human,self.level).compMove()
