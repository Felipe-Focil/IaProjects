import copy
import Board as bd
import Search as sh
import Point as pt
import Graph as gp


class Algorithm:
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.boardOriginal = copy.deepcopy(board)
        self.found = False
        self.board = board
        self.algo = ""

    def BFS(self):
        search = sh.Search(self.board)
        self.found = search.BFS(self.board.start, self.board.goal)
        search.board.showPath(self.board.goal)
        self.algo = "Breath First Search"

    def DFS(self):
        search = sh.Search(self.board)
        self.found = search.DFS(self.board.start, self.board.goal)
        search.board.showPath(self.board.goal)
        self.algo = "Depth First Search"

    def Hill(self):
        search = sh.Search(self.board)
        self.board.setW()
        self.found = search.Hill(self.board.start, self.board.goal)
        self.algo = "Hill Climbing Search"

    def Best(self):
        search4 = sh.Search(self.board)
        self.board.setW()
        self.found = search4.BestFS(self.board.start, self.board.goal)
        self.algo = "Best First Search"

    def A(self):
        search4 = sh.Search(self.board)
        self.board.setW()
        self.found = search4.BestFS(self.board.start, self.board.goal)

        self.algo = "A*"

    def showAlgorithm(self):
        self.board.setStart(self.board.start)
        self.board.setGoal(self.board.goal)
        g = gp.Graph(self.boardOriginal, self.board)
        g.add(self.algo, self.found)

        g.updateGraph()
