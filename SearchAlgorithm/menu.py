import Algorithm as al
import Sample as samp


class Menu:
    def __init__(self):
        sample = samp.Sample()
        self.board = sample.Hill()
        self.main = al.Algorithm(sample.BFS())

    def setBoard(self, board):
        self.board = board

    def setSampleBoard(self, num):
        sample = samp.Sample()
        if num == 1:
            self.board = sample.BFS()
        elif num == 2:
            self.board = sample.DFS()
        elif num == 3:
            self.board = sample.Hill()
        elif num == 4:
            self.board = sample.Best()
        elif num == 5:
            self.board = sample.A()

    def setAlgorithm(self, num):
        self.main = al.Algorithm(self.board)

        if num == 1:
            self.main.BFS()
        elif num == 2:
            self.main.DFS()
        elif num == 3:
            self.main.Hill()
        elif num == 4:
            self.main.Best()
        elif num == 5:
            self.main.A()

    def run(self):
        self.main.showAlgorithm()

    def show(self):
        print("Select a Sample Board: ")
        brd = int(input())
        print("1.BFS\n2.DFS\n3.Hill\n4.Best\n5.A*\nSelect Algorithm: ")
        alg = int(input())
        self.setSampleBoard(brd)
        self.setAlgorithm(alg)
        self.run()
        print("Exit? \n0.Yes \n1.No")
        opt = int(input())
        return opt
