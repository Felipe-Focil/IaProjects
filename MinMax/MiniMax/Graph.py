import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Graph:

    def transformBoard(self, b):
        board = [[0 for _ in range(0, 3)] for _ in range(0, 3)]
        empty = 0
        O = 1
        X = 2

        for i in range(0, 3):
            for j in range(0, 3):
                if b.board[i][j] == '.':
                    board[i][j] = 3
                elif b.board[i][j] == 'O':
                    board[i][j] = 2
                elif b.board[i][j] == 'X':
                    board[i][j] = 1
        return board

    def show(self, board, played, status):

        a = self.transformBoard(board)
        fig, self.ax = plt.subplots()
        ln = self.ax.matshow(a)
        self.ax.set_title(played + " played")
        self.ax.set_xlabel(status)

        plt.show()
