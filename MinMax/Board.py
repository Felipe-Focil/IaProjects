import Player as pl
import Point as pt


class Board:
    def __init__(self):
        self.a = pl.Player('O')
        self.b = pl.Player('X')
        self.board = ['.'] * 3
        for i in range(0, 3):
            self.board[i] = ['.'] * 3

    def shortCut(self, move):
        """
        [1][2][3]
        [4][5][6]
        [7][8][9]
        """
        if move == 1:
            return pt.Point(0, 0)
        elif move == 2:
            return pt.Point(0, 1)
        elif move == 3:
            return pt.Point(0, 2)
        elif move == 4:
            return pt.Point(1, 0)
        elif move == 5:
            return pt.Point(1, 1)
        elif move == 6:
            return pt.Point(1, 2)
        elif move == 7:
            return pt.Point(2, 0)
        elif move == 8:
            return pt.Point(2, 1)
        elif move == 9:
            return pt.Point(2, 2)

    def getValue(self, coord):
        point = self.shortCut(coord)
        return self.board[point.y][point.x]

    def setValue(self, coord, value):
        point = self.shortCut(coord)
        self.board[point.y][point.x] = value

    def show(self):
        for i in range(0, 3):
            print("[", end="")
            for j in range(0, 3):
                print(self.board[i][j], end="")
            print("]")
        print("\n")

    def isWin(self, result):
        if result == '.':
            return False
        return True

    def check(self, a, inc):
        prev = self.getValue(a)
        for i in range(0, 3):
            if self.getValue(a) == '.':
                return '.'
            elif self.getValue(a) != prev:
                return '.'
            a = a + inc
        return prev

    def winHorizontal(self):
        if self.isWin(self.check(1, 1)):
            return self.check(1, 1)
        if self.isWin(self.check(4, 1)):
            return self.check(4, 1)
        if self.isWin(self.check(7, 1)):
            return self.check(7, 1)
        return '.'

    def winVertical(self):
        if self.isWin(self.check(1, 3)):
            return self.check(1, 3)
        if self.isWin(self.check(2, 3)):
            return self.check(2, 3)
        if self.isWin(self.check(3, 3)):
            return self.check(3, 3)
        return '.'

    def winDiagonal(self):
        if self.isWin(self.check(1, 4)):
            return self.check(1, 4)
        if self.isWin(self.check(3, 2)):
            return self.check(3, 2)
        return '.'

    def whoWin(self):
        h = self.winHorizontal()
        v = self.winVertical()
        d = self.winDiagonal()
        if h != '.':
            return h
        elif v != '.':
            return v
        elif d != '.':
            return d
        return '.'

    def somebodyWin(self):
        if self.whoWin() != '.':
            return True
        return False

    def isDraw(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    return False
        if self.whoWin() == '.':
            return True
        return False

    def isValid(self, move):
        if self.getValue(move) == '.':
            return True
        return False
