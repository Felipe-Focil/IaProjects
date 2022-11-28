import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Board as bd
import Search as sh
import Point as p


class Graph:

    def __init__(self, board, transform):
        self.board = board
        self.transform = transform
        self.notVisited = 5  # Not Visited
        self.visited = 1  # Visited
        self.path = 4  # Path
        self.obstacle = 0  # Obstacle
        self.start = 2  # Start
        self.goal = 3  # Goal

    def add(self, algorithm, found):
        self.algorithm = algorithm
        self.found = found

    def transformBoard(self, b):
        board = [[1 for _ in range(b.n)] for _ in range(b.m)]

        for i in range(b.n):
            for j in range(b.m):
                v = b.board[i][j].val
                if v == '.':
                    board[i][j] = self.notVisited
                elif v == '#':
                    board[i][j] = self.obstacle
                elif v == 'G':
                    board[i][j] = self.goal
                elif v == 'S':
                    board[i][j] = self.start
                elif v == 'P':
                    board[i][j] = self.path
                elif v == 'V':
                    board[i][j] = self.visited

        return board

    def updateGraph(self):

        a = self.transformBoard(self.board)

        fig, self.ax = plt.subplots()
        ln = self.ax.matshow(a)
        self.ax.set_title(self.algorithm)
        self.ax.set_xlabel("Searching...")

        def artist():
            return len

        def update(frame):
            self.ax.clear()

            a = self.transformBoard(self.transform)
            self.ax.matshow(a)
            self.ax.set_xlabel(str(self.found))
            self.ax.set_title(self.algorithm)

        animation = FuncAnimation(
            fig, update, interval=4500, init_func=artist, repeat=False)

        plt.show()


"""
board = bd.Board(5, 5)

board.addObstacule(p.Point(3, 4, 0))
#board.addObstacule(p.Point(3, 3, 0))
board.addObstacule(p.Point(1, 2, 0))
board.addObstacule(p.Point(1, 3, 0))
board.addObstacule(p.Point(2, 3, 0))
board.addObstacule(p.Point(3, 1, 0))
board.addObstacule(p.Point(3, 2, 0))

board.setStart(p.Point(2, 4, 0))
board.setGoal(p.Point(4, 4, 0))

boardOriginal = bd.Board(5, 5)

boardOriginal.addObstacule(p.Point(3, 4, 0))
boardOriginal.addObstacule(p.Point(3, 3, 0))
boardOriginal.addObstacule(p.Point(1, 2, 0))
boardOriginal.addObstacule(p.Point(1, 3, 0))
boardOriginal.addObstacule(p.Point(2, 3, 0))
boardOriginal.addObstacule(p.Point(3, 1, 0))
boardOriginal.addObstacule(p.Point(3, 2, 0))

boardOriginal.setStart(p.Point(2, 4, 0))
boardOriginal.setGoal(p.Point(4, 4, 0))

search = sh.Search(board)
found = search.DFS(board.start, board.goal)
search.board.showPath(board.goal)
"""
"""
board = bd.Board(5, 5)

board.addObstacule(p.Point(3, 1, 0))
board.addObstacule(p.Point(3, 2, 0))
board.addObstacule(p.Point(3, 3, 0))

#board.addObstacule(p.Point(1, 1, 0))
#board.addObstacule(p.Point(2, 1, 0))

board.setStart(p.Point(1, 0, 0))
board.setGoal(p.Point(4, 2, 0))


search4 = sh.Search(board)


board.setW()
found = search4.BestFS(board.start, board.goal)

board4 = bd.Board(5, 5)

board4.addObstacule(p.Point(3, 1, 0))
board4.addObstacule(p.Point(3, 2, 0))
board4.addObstacule(p.Point(3, 3, 0))

#board4.addObstacule(p.Point(1, 1, 0))
#board4.addObstacule(p.Point(2, 1, 0))

board4.setStart(p.Point(1, 0, 0))
board4.setGoal(p.Point(4, 2, 0))


g = Graph(board4, board)
g.add("Best First", found)

g.updateGraph()
"""
