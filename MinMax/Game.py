import Board as bd
import Player as pl
import Graph as gp
import Algorithm as al


class Game:
    def __init__(self):
        self.board = bd.Board()
        self.playerO = pl.Player('O')
        self.playerX = pl.Player('X')

    def setHuman(self, player):
        if player == 'O':
            self.human = self.playerO
            self.IA = self.playerX
        else:
            self.human = self.playerX
            self.IA = self.playerO

    def isHuman(self, player):
        if player == self.human:
            return True
        return False

    def setAlgorithm(self, level):
        self.level = level
        self.alg = al.Algorithm(self.board, level,self.human.piece,self.IA.piece)

    def setTurn(self, player):
        if player == self.playerO:
            self.turn = self.playerO
            self.playerO.turn = True
            self.playerX.turn = False
        else:
            self.turn = self.playerX
            self.playerX.turn = True
            self.playerO.turn = False

    def passTurn(self, player):
        if player == self.playerO:
            self.setTurn(self.playerX)
        else:
            self.setTurn(self.playerO)

    def getTurn(self):
        return self.turn

    def setFirst(self, player):
        if player == 'O':
            self.setTurn(self.playerO)
            self.turn = self.playerO
        else:
            self.setTurn(self.playerX)
            self.turn = self.playerX

    def playHuman(self):
        valid = False
        val = 0
        while not valid:
            val = int(input("Play : "))
            if self.board.isValid(val):
                valid = True
        self.board.setValue(val, self.human.piece)
        self.passTurn(self.human)

    def playIA(self):
        self.setAlgorithm(self.level)
        val = self.alg.getValue()
        self.board.setValue(val, self.IA.piece)
        self.passTurn(self.IA)

    def whoIsPlaying(self):
        if self.isHuman(self.getTurn()):
            return "Computer"
        else:
            return "Human"

    def getStatus(self):
        if self.board.somebodyWin():
            return "Won " + self.board.whoWin()
        elif self.board.isDraw():
            return "Draw"
        else:
            return "Playing"

    def play(self):
        g = gp.Graph()
        while not self.board.somebodyWin() or not self.board.isDraw():
            if self.isHuman(self.getTurn()):
                self.playHuman()
            else:
                self.playIA()
            g.show(self.board, self.whoIsPlaying(), self.getStatus())
            if self.board.somebodyWin():
                break
            elif self.board.isDraw():
                break
