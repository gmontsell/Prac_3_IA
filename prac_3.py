def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def startGame(symbol):
    bestScore = -800
    for key in board.keys(): #Checks every move, for every move creates the minimax
        if (board[key] == ' '):
            board[key] = symbol
            isMaximizing = (symbol == 'O')
            print("------------------------")
            score = minimax(board, 0, isMaximizing)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
    return

def minimax(board, depth, isMaximizing):
    print("Profunditat espai d'estas: ",depth+1)
    printBoard(board)
    if (checkWhichMarkWon(maxi)):
        count_prob[1] += 1
        return 1
    elif (checkDraw()):
        return 0
    elif (checkWhichMarkWon(mini)):
        count_prob[1] -= 1
        return -1

    if (isMaximizing):
        bestScore = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = maxi
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = mini
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: 'X', 2: ' ', 3: 'O', 
         4: 'X', 5: 'O', 6: 'X', 
         7: ' ', 8: ' ', 9: ' '}

print("INITIAL STATE")
printBoard(board)
print("FI")
mini = 'O'
maxi = 'X'
count_prob = {1: 0}
startGame('O')
print("Si comparem els resultat de l'espai d'estats és: ",count_prob[1])
print("Per tant té més possibilitats de guanyar el jugador: ","O" if count_prob[1] < 0 else "X")
