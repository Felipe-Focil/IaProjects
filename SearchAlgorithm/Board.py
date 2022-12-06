import Point as p
import math


class Board:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.start = None
        self.goal = None
        self.board = [None] * self.n
        for i in range(0, self.n):
            self.board[i] = [None] * self.m

        for i in range(0, n):
            for j in range(0, m):
                self.board[i][j] = p.Point(i+1, j+1, 0)

        self.clear()

    def clear(self):
        self.mainPath = [False] * self.n
        for i in range(0, self.n):
            self.mainPath[i] = [False] * self.m

        self.visited = [False] * self.n
        for i in range(0, self.n):
            self.visited[i] = [False] * self.m

        self.path = [None] * self.n
        for i in range(0, self.n):
            self.path[i] = [None] * self.m

        for i in range(0, self.n):
            for j in range(0, self.m):
                self.path[i][j] = p.Point(0, 0, 0)

    def addObstacule(self, point):
        self.board[point.y][point.x].updateVal('#')

    def isVisited(self, point):
        if self.visited[point.y][point.x] is True:
            return True
        return False

    def markVisited(self, point):
        self.visited[point.y][point.x] = True
        self.board[point.y][point.x].val = 'V'

    def markMainPath(self, p):
        self.mainPath[p.y][p.x] = True
        self.board[p.y][p.x] = 'P'

    def showMainPath(self):
        for i in range(self.n):
            print("[", end="")
            for j in range(self.m):
                v = self.mainPath[i][j]
                if v:
                    print(1, end=",")
                else:
                    print(0, end=",")
            print("]")
        print("\n")

    def markParent(self, father, child, t):
        self.path[child.y][child.x] = father
        self.path[child.y][child.x].t = t+1

    def showParent(self, point):
        if point.t != 0:
            print("(" + str(point.x) + "," + str(point.y) +
                  "," + str(point.t) + ")", end=",")
        else:
            print("( , , )", end=",")

    def comparePoints(self, a, b):
        #print(a.toString() + "=" + b.toString())
        if a.x is b.x and a.y is b.y:
            return True
        return False

    def setGoal(self, point):
        self.goal = p.Point(point.x, point.y, 0)
        self.board[self.goal.y][self.goal.x].updateVal('G')
        self.setW()
        self.goal.setW(self.board[point.y][point.x].w)

    def setStart(self, point):
        self.start = p.Point(point.x, point.y, 0)
        self.board[point.y][point.x].updateVal('S')
        self.start.setW(self.board[point.y][point.x].w)

    def getValue(self, point):
        return self.board[point.y][point.x].val

    def showBoard(self, board):
        for i in range(self.n):
            print("[", end="")
            for j in range(self.m):
                print(board[i][j].val, end=",")
            print("]\n")

    def showBoardPath(self):
        for i in range(self.n):
            print("[", end="")
            for j in range(self.m):
                self.showParent(self.path[i][j])
            print("]")

    def showBoardW(self):
        for i in range(self.n):
            print("[", end="")
            for j in range(self.m):
                print(self.board[i][j].w, end=",")
            print("]")

    def showBoards(self):
        self.showBoard(self.board)
        self.showVisited()
        self.showBoardW()
        self.showBoardPath()

    def showVisited(self):
        for i in range(self.n):
            print("[", end="")
            for j in range(self.m):
                v = self.visited[i][j]
                if v:
                    print(1, end=",")
                else:
                    print(0, end=",")
            print("]")
        print("\n")

    def Sucesors(self, point):  # Añade todos los posibles sucesores
        point.Up()
        point.Down(self.n)
        point.Right(self.m)
        point.Left()

        for i in point.sucesor:
            i.setW(self.board[i.x][i.y].w)
        return point.sucesor

    def showPath(self, father):
        if self.path[father.y][father.x].t != 0:
            self.board[father.y][father.x].val = 'P'
            self.showPath(self.path[father.y][father.x])

    def showBoardPath(self):
        self.showBoard(self.path)

    def addW(self, a, b, c, d, w):
        self.board[b][a].sucesor = self.board[b][a].setW(self.board[d][c], w)

    def getDistance(self, x, y):
        return abs(abs(self.goal.x - x) + abs(self.goal.y - y))

    def setW(self):
        for i in range(self.n):
            for j in range(self.m):
                self.board[i][j].setW(self.getDistance(j, i))
