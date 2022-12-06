import Board
import copy


class MiniMax:

    def __init__(self, board, ia, human, dif):
        self.board = board
        self.dif = dif
        self.human = human
        self.ia = ia

    def getMove(self):
        bestScore = -1000
        bestMove = 1
        for i in range(1, 9):
            if self.board.isValid(i):
                print(i)
                board = copy.deepcopy(self.board)
                board.setValue(i, self.ia)
                score = self.miniMax(board, 0, False)
                print(score)
                self.board.setValue(i, '.')
                if score > bestScore:
                    bestScore = score
                    bestMove = i
        return bestMove

    def getScore(self, char):
        if char == 'X':
            return int(1)
        else:
            return (-1)

    def compMove(self):

        bestVal = -1000
        bestMove = 0
        for i in range(9):
            if self.board.isValid(i):
                self.board.setValue(i, self.ia)
                board = copy.deepcopy(self.board)
                val = minimax(board, 0, False)
                self.board.setValue(i, '.')
                if (val > bestVal):
                    bestVal = val
                    bestMove = i

        self.board.setValue(self.ia, bestMove)
        return


def minimax(self, board, depth, isMaximizing):

    # if(self.dif == 0 and depth == 2):
    # return scoreTab(board)
    # elif(self.dif == 1 and depth == 4):
    # return scoreTab(board)
    if (board.somebodyWin()):
        return self.getScore(board.whoWin())
    elif (board.isDraw()):
        return 0

    if (isMaximizing):
        bestVal = -1000
        for i in range(9):
            if (board[i] == i):
                board.setValue(i, self.ia)
                newBoard = copy.deepcopy(self.board)
                val = minimax(newBoard, depth + 1, False)
                board.setValue(i, '.')
                if (val > bestVal):
                    bestVal = val
        return bestVal

    else:
        bestVal = 1000
        for i in range(9):
            if board.isValid(i):
                board.setValue(i, self.human)
                newBoard = copy.deepcopy(self.board)
                val = minimax(newBoard, depth + 1, True)
                board.setValue(i, '.')
                if (val < bestVal):
                    bestVal = val
        return bestVal
    """
    def miniMax(self, board, depth, max):
        if board.somebodyWin():
            return self.getScore(board.whoWin())
        elif board.isDraw():
            return 0
        board.show()
        # board.show()
        for i in range(1, 9):
            if board.isValid(i):
                if max:
                    bestScore = -1001
                    board.setValue(i, self.ia)
                    score = self.miniMax(
                        board, depth + 1, True)
                    board.setValue(i, '.')
                    bestScore = max(score, bestScore)
                else:
                    bestScore = 1001
                    board.setValue(i, self.getHuman())
                    score = self.miniMax(board, depth + 1, False)
                    board.setValue(i, '.')
                    bestScore = min(score, bestScore)
        return bestScore
    """
