class Player:
    def __init__(self, piece):
        self.piece = piece
        self.turn = False
        self.win = 0

    def play(board, move):
        board.set(move)
