import Graph as gp

g = gp.Graph()
color = int(("Select Color you want to play: "))

if color == 0:
    player = 'O'
    bot = 'X'
else:
    player = 'X'
    bot = 'O'


def spaceIsFree(position):
    if board[position] == position:
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        status = "Playing..."
        played = ""
        if letter == player:
            played = "Human"
        else:
            played = "Bot"

        if (checkDraw()):
            print("Draw!")
            status = "Draw"
            exit()
        if checkForWin():
            if letter == bot:
                status = "Bot Wins!"
            else:
                status = "Player Wins!"

        g.show(board,played,status)

        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    if (board[0] == board[1] and board[0] == board[2] and board[0] != 1):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] != 4):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] != 7):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] != 1):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != 2):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != 3):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] != 1):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] != 7):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[0] == board[1] and board[0] == board[2] and board[0] == mark:
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] == mark):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == mark):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] == mark):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] == mark):
        return True
    else:
        return False


def checkDraw():
    for i in range(9):
        if (board[i] == i):
            return False
    return True


def playerMove():
    position = int(input("Player's Turn (O)  "))
    insertLetter(player, position)
    return


def compMove():
    print("Computer's Turn (X) ")
    bestVal = -1000
    bestMove = 0
    for i in range(9):
        if (board[i] == i):
            board[i] = bot
            val = minimax(board, 0, False)
            board[i] = i
            if (val > bestVal):
                bestVal = val
                bestMove = i

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):

    if(dif == 0 and depth == 2):
        return scoreTab(board)
    elif(dif == 1 and depth == 4):
        return scoreTab(board)
    elif (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestVal = -1000
        for i in range(9):
            if (board[i] == i):
                board[i] = bot
                val = minimax(board, depth + 1, False)
                board[i] = i
                if (val > bestVal):
                    bestVal = val
        return bestVal

    else:
        bestVal = 1000
        for i in range(9):
            if (board[i] == i):
                board[i] = player
                val = minimax(board, depth + 1, True)
                board[i] = i
                if (val < bestVal):
                    bestVal = val
        return bestVal


def scoreTab(board):
    score = 0
    taparScore = 2

    # verticals
    if board[0] == 1 and board[3] == 1 and board[6] == 0:
        score += 1
    if board[1] == 1 and board[4] == 1 and board[7] == 0:
        score += 1
    if board[2] == 1 and board[5] == 1 and board[8] == 0:
        score += 1

    if board[0] == 1 and board[3] == 0 and board[6] == 1:
        score += 1
    if board[1] == 1 and board[4] == 0 and board[7] == 1:
        score += 1
    if board[2] == 1 and board[5] == 0 and board[8] == 1:
        score += 1

    if board[0] == 0 and board[3] == 1 and board[6] == 1:
        score += 1
    if board[1] == 0 and board[4] == 1 and board[7] == 1:
        score += 1
    if board[2] == 0 and board[5] == 1 and board[8] == 1:
        score += 1

    # horizontal
    if board[0] == 1 and board[1] == 1 and board[2] == 0:
        score += 1
    if board[3] == 1 and board[4] == 1 and board[5] == 0:
        score += 1
    if board[6] == 1 and board[7] == 1 and board[8] == 0:
        score += 1

    if board[0] == 1 and board[1] == 0 and board[2] == 1:
        score += 1
    if board[3] == 1 and board[4] == 0 and board[5] == 1:
        score += 1
    if board[6] == 1 and board[7] == 0 and board[8] == 1:
        score += 1

    if board[0] == 0 and board[1] == 1 and board[2] == 1:
        score += 1
    if board[3] == 0 and board[4] == 1 and board[5] == 1:
        score += 1
    if board[6] == 0 and board[7] == 1 and board[8] == 1:
        score += 1

    # diagonal
    if board[0] == 1 and board[4] == 1 and board[8] == 0:
        score += 1
    if board[0] == 1 and board[4] == 0 and board[8] == 1:
        score += 1
    if board[0] == 0 and board[4] == 1 and board[8] == 1:
        score += 1

    if board[6] == 1 and board[4] == 1 and board[2] == 0:
        score += 1
    if board[6] == 1 and board[4] == 0 and board[2] == 1:
        score += 1
    if board[6] == 0 and board[4] == 1 and board[2] == 1:
        score += 1

    # tapa al jugador

    # horizontal
    if board[0] == 1 and board[1] == 2 and board[2] == 2:
        score += taparScore
    if board[0] == 2 and board[1] == 1 and board[2] == 2:
        score += taparScore
    if board[0] == 2 and board[1] == 2 and board[2] == 1:
        score += taparScore

    if board[3] == 1 and board[4] == 2 and board[5] == 2:
        score += taparScore
    if board[3] == 2 and board[4] == 1 and board[5] == 2:
        score += taparScore
    if board[3] == 2 and board[4] == 2 and board[5] == 1:
        score += taparScore

    if board[6] == 1 and board[7] == 2 and board[8] == 2:
        score += taparScore
    if board[6] == 2 and board[7] == 1 and board[8] == 2:
        score += taparScore
    if board[6] == 2 and board[7] == 2 and board[8] == 1:
        score += taparScore

    # diagonal
    if board[0] == 1 and board[4] == 2 and board[8] == 2:
        score += taparScore
    if board[0] == 2 and board[4] == 1 and board[8] == 2:
        score += taparScore
    if board[0] == 2 and board[4] == 2 and board[8] == 1:
        score += taparScore

    if board[6] == 1 and board[4] == 2 and board[2] == 2:
        score += taparScore
    if board[6] == 2 and board[4] == 1 and board[2] == 2:
        score += taparScore
    if board[6] == 2 and board[4] == 2 and board[2] == 1:
        score += taparScore

    return score


# game board

# Thinks that I modified
def printBoardOption(board):
    print("\n")
    print(6, "|", 7, "|", 8)
    print("----------")
    print(3, "|", 4, "|", 5)
    print("----------")
    print(0, "|", 1, "|", 2)
    print("\n")


board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

printBoardOption(board)



global firstComputerMove
firstComputerMove = True

choice = int(input("Who is playing first? (0: you, 1:computer): "))
dif = int(input("Difficulty? (0: easy, 1: hard, 2: expert): "))
if(choice == 1):
    while not checkForWin():
        compMove()
        playerMove()
else:
    while not checkForWin():
        playerMove()
        compMove()
