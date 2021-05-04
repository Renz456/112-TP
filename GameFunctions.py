# Helper functions for running the game

# checks if move outflanks opposing teams piece
def checkOutflank(app, row, col, dire, board, player):
    tempRow = row + dire[0]
    tempCol = col +dire[1]
    checkCol = ''
    if player:
       checkCol = app.p1Color
    else:
        checkCol = app.p2Color
    while ((0<=tempRow<app.rows and 0<=tempCol<app.cols)
            and board[tempRow][tempCol]):
        if board[tempRow][tempCol] == checkCol:
            return True
        tempRow += dire[0]
        tempCol += dire[1]
        
    return False

# checks if move is legal
def isMoveLegal(app, row, col, board, player):
    checkColor = ''
    color = ''
    if player:
        checkColor = app.p2Color
    else:
        checkColor = app.p1Color
    possibleAdj = [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]
    legal = False
    for check in possibleAdj:
        if (0<=row+check[0]<app.rows and 0<=col+check[1]<app.cols
            and board[row+check[0]][col+check[1]]==checkColor):
            if checkOutflank(app, row, col, check, board, player):
                legal = True
    return legal

# Flips pieces when a move is made
def flipPieces(app, row, col, board):
    checkDir = [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]
    flipDir = []
    checkCol = board[row][col]
    checkCol2 = ''
    if checkCol == app.p1Color:
        checkCol2 = app.p2Color
    else: checkCol2 = app.p1Color
    
    for dire in checkDir:
        tempRow = row + dire[0]
        tempCol = col + dire[1]
        if (0<= tempRow < app.rows and 0<= tempCol < app.cols and 
            board[tempRow][tempCol]==checkCol2):
            while ((0<= tempRow < app.rows and 0<= tempCol < app.cols)
                    and board[tempRow][tempCol]):
                if (board[tempRow][tempCol] == checkCol):
                    flipDir.append(dire)
                tempRow += dire[0]
                tempCol += dire[1]

    for dire in flipDir:
        tempRow = row + dire[0]
        tempCol = col + dire[1]
        while board[tempRow][tempCol] != checkCol:
            board[tempRow][tempCol] = checkCol
            tempRow += dire[0]
            tempCol += dire[1]

# checks if there's a legal move for the other player before switching turns
def canSwitch(app, player, board):
    player = not player
    for i in range(app.rows):
        for j in range(app.cols):
            if (not board[i][j] and 
                isMoveLegal(app, i, j, board, player)):
                return True
    print('no switch')
    return False