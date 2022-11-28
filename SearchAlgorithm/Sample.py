
import Board as bd
import Search as sh
import Point as pt
import Graph as gp
import Point as p


class Sample:

    def __init__(self):
        a = 2

    def BFS(self):
        board = bd.Board(5, 5)
        board.addObstacule(p.Point(3, 4, 0))
        board.addObstacule(p.Point(3, 3, 0))
        board.addObstacule(p.Point(1, 2, 0))
        board.addObstacule(p.Point(1, 3, 0))
        board.addObstacule(p.Point(2, 3, 0))
        board.addObstacule(p.Point(3, 1, 0))
        board.addObstacule(p.Point(3, 2, 0))

        board.setStart(p.Point(2, 4, 0))
        board.setGoal(p.Point(4, 4, 0))
        return board

    def DFS(self):
        board1 = bd.Board(200, 200)

        board1.addObstacule(p.Point(0, 1, 0))
        board1.addObstacule(p.Point(0, 3, 0))
        board1.addObstacule(p.Point(1, 1, 0))
        board1.addObstacule(p.Point(1, 3, 0))
        board1.addObstacule(p.Point(3, 1, 0))
        board1.addObstacule(p.Point(3, 3, 0))
        board1.addObstacule(p.Point(4, 1, 0))
        board1.addObstacule(p.Point(4, 3, 0))

        board1.setStart(p.Point(2, 2, 0))
        board1.setGoal(p.Point(0, 5, 0))
        return board1

    def Hill(self):
        board4 = bd.Board(5, 5)

        board4.addObstacule(p.Point(3, 1, 0))
        board4.addObstacule(p.Point(3, 2, 0))
        board4.addObstacule(p.Point(3, 3, 0))

        #board4.addObstacule(p.Point(1, 1, 0))
        board4.addObstacule(p.Point(2, 1, 0))

        board4.setStart(p.Point(1, 0, 0))
        board4.setGoal(p.Point(4, 2, 0))
        return board4

    def Best(self):
        board4 = bd.Board(5, 5)

        board4.addObstacule(p.Point(3, 1, 0))
        board4.addObstacule(p.Point(3, 2, 0))
        board4.addObstacule(p.Point(3, 3, 0))

        #board4.addObstacule(p.Point(1, 1, 0))
        #board4.addObstacule(p.Point(2, 1, 0))

        board4.setStart(p.Point(1, 0, 0))
        board4.setGoal(p.Point(4, 2, 0))
        return board4

    def A(self):
        board4 = bd.Board(5, 5)

        board4.addObstacule(p.Point(3, 1, 0))
        board4.addObstacule(p.Point(3, 2, 0))
        board4.addObstacule(p.Point(3, 3, 0))

        #board4.addObstacule(p.Point(1, 1, 0))
        board4.addObstacule(p.Point(2, 1, 0))

        board4.setStart(p.Point(1, 0, 0))
        board4.setGoal(p.Point(4, 2, 0))
        return board4
