import Board as bd
import Game as gm

board = bd.Board()
game = gm.Game()

game.setHuman('O')
game.setFirst('O')
game.setAlgorithm(0)

game.play()
