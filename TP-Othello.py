# TO DO:
# - Helper Functions: checkOutflank, canSwitch, checkWin DONE!
# - Write minimax alg (Work in Progress)
# - Function to determine "score" of the game for minimaxAlg DONE! (sorta)
# - Fix buttons on homepage and make homepage look nicer
# - Error messages while playing? (like invalid move no flips or smth) 
# - decide "cool" mode to include
# - include settings page to change colour etc.
# - Extra: add sound (bg music, every time a piece is placed/flipped) 
#          flipping animation? Leaderboad for beating AI?
# - Sockets? for multiple computers
# - Hints for 2 player? (could use the same minimax alg)
# - different shaped boards for cool feature with obstacles?
# Other more complex heuristics for minimax?

from cmu_112_graphics import *
import tkinter as tk

def appStarted(app):
    app.rows = 8
    app.cols = 8
    app.bColor = 'Green'
    app.p1Color = 'Black'
    app.p2Color = 'White'
    playGame(app)
    app.home = True
    app.play = False
    createHome(app)

def createHome(app):
    app.buttonSize = app.width//10
    app.bx0 = app.width//3
    app.bx1 = app.width*2//3
    app.b1y0 = app.height*5//16
    app.b1y1 = app.height*7//16
    app.b2y0 = app.b1y1 + app.height//16
    app.b2y1 = app.b2y0 + app.height*2//16
    app.b3y0 = app.b2y1 + app.height//16
    app.b3y1 = app.b3y0 + app.height*2//16

def playGame(app):
    app.board = []
    for i in range(app.rows):
        app.board += [[None]*app.rows]
    app.board[app.rows//2-1][app.cols//2-1] = app.p2Color
    app.board[app.rows//2-1][app.cols//2] = app.p1Color
    app.board[app.rows//2][app.cols//2] = app.p2Color
    app.board[app.rows//2][app.cols//2-1] = app.p1Color
    app.margin = app.width//10
    app.size = (app.width-2*app.margin)//8
    app.player = True
    # True is black False is white
    app.over = False
    # Used this for a test case
    # app.board = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', None],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'White'],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'White', 'White', 'White'],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'White', None, None],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'White', None, None],
    #             ['Black', 'Black', 'Black', 'Black', 'Black', 'White', None, None]] 
    app.Ai = False  

def playAi(app):
    playGame(app)
    app.ez = False
    app.med = False
    app.hard = False
    app.choose = True
    app.play = False
    # setting this ^ as false for now until i finish the entire alg

# checks if move outflanks opposing teams piece
def checkOutflank(app, row, col, dire, board, player):
    tempRow = row + dire[0]
    tempCol = col +dire[1]
    checkCol = ''
    if player:
       checkCol = 'Black'
    else:
        checkCol = 'White'
    while 0<=tempRow<app.rows and 0<=tempCol<app.cols:
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
        checkColor = 'White'
    else:
        checkColor = 'Black'
    possibleAdj = [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]
    legal = False
    for check in possibleAdj:
        if (0<=row+check[0]<app.rows and 0<=col+check[1]<app.cols
            and board[row+check[0]][col+check[1]]==checkColor):
            if checkOutflank(app, row, col, check, board, player):
                legal = True
        
        # Debug Stuff
        # else:
        #     if 0<row+check[0]<app.rows and 0<col+check[1]<app.cols:
        #         print('out of bounds')
        #     else:
        #         print(app.board[row+check[0]][col+check[1]]==checkColor)
        #         print(app.board[row+check[0]][col+check[1]]==checkColor)
        #     print('check 70')
        #     print(checkColor)
        #     print(check)
    return legal

def flipPieces(app, row, col, board):
    checkDir = [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]
    flipDir = []
    checkCol = board[row][col]
    checkCol2 = ''
    if checkCol == 'Black':
        checkCol2 = 'White'
    else: checkCol2 = 'Black'
    
    for dire in checkDir:
        tempRow = row + dire[0]
        tempCol = col + dire[1]
        if (0<= tempRow < app.rows and 0<= tempCol < app.cols and 
            board[tempRow][tempCol]==checkCol2):
            while 0<= tempRow < app.rows and 0<= tempCol < app.cols:
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
                isMoveLegal(app, i, j, board, app.player)):
                return True
    print('no switch')
    return False

# checks if game over and returns winner's score
def checkWin(app, board):
    for i in range(app.rows):
        for j in range(app.cols):
            if (not board[i][j] and 
                (isMoveLegal(app, i, j, board, True) or 
                isMoveLegal(app, i, j, board, False))): 
                return False
    return True

# Heuristics Below
# Assumes that AI is always white for now

# Count's score by only evaluating number of pieces
def ezScore(app, board):
    scoreW = 0
    scoreB = 0
    for i in range(app.rows):
        for j in range(app.cols):
            if board[i][j] == 'White':
                scoreW += 1
            elif board[i][j] == 'Black':
                scoreB += 1
    return scoreW - scoreB

# weights corners and edge pieces more (5 and 3 respectively)
def medScore(app, board):
    scoreW = 0
    scoreB = 0
    corner = 5
    edge = 3
    mid = 1
    for i in range(app.rows):
        for j in range(app.cols):
            add = 0
            if not board[i][j]: 
                if ((i==0 and j == 0) or (i == app.rows-1 and j == app.cols-1) 
                    or (i == 0 and j == app.cols-1) or (i == app.rows-1 and j == 0)):
                    add = corner
                elif (i == 0 or j == 0 or i == app.rows-1 or j == app.cols-1):
                    add = edge
                else: add = mid
            if board[i][j] == 'White':
                scoreW += add
            elif board[i][j] == 'Black':
                scoreB += add
    return scoreW-scoreB

def hardScore(app, board):
    # Corners and edges weighted more, 10 for corners 3 for edge
    # adjacents to opposite corners weighted as negative
    # Other possible weightage = [4, -3, 2, 2, 2, 2, -3, 4,
                            #    -3, -4, -1, -1, -1, -1, -4, -3,
                            #    2, -1, 1, 0, 0, 1, -1, 2,
                            #    2, -1, 0, 1, 1, 0, -1, 2,
                            #    2, -1, 0, 1, 1, 0, -1, 2,
                            #    2, -1, 1, 0, 0, 1, -1, 2,
                            #    -3, -4, -1, -1, -1, -1, -4, -3,
                            #    4, -3, 2, 2, 2, 2, -3, 4]
    # Got that ^ from https://github.com/hylbyj/Alpha-Beta-Pruning-for-Othello-Game/blob/master/readme_alpha_beta.txt
    scoreB = 0
    scoreW = 0
    opponent = 'Black'
    corner = 10
    adj = 3
    normal = 1
    for i in range(app.rows):
        for j in range(app.cols):
            add = 0
            if not board[i][j]:
                if ((i==0 and j == 0) or (i == app.rows-1 and j == app.cols-1) 
                    or (i == 0 and j == app.cols-1) or (i == app.rows-1 and j == 0)):
                    add = corner
                elif (((i == 0 and j == 1) or (i == 1 or j == 0)) 
                        and board[0][o] == opponent):
                    add = -adj
                elif (((i == app.rows-2 and j == 0) or (i == app.rows-1 and j == 1)) and 
                    board[app.rows-1][0]==opponent):
                    add = -adj
                elif (((i == 0 and j == app.cols-2) or 
                        (i == 1 and j == app.cols-1)) and 
                        board[0][app.cols-1]==opponent):
                    add = -adj
                elif ((i == app.rows-1 and j == app.cols-2) or 
                    (i == app.rows-2 and j == app.cols-1) and 
                    board[app.rows-1][app.cols-1] == opponent):
                    add = -adj
                elif (i == 0 or j == 0 or i == app.rows-1 or j == app.cols-1) :
                    add = adj
                else: add = 1
            if board[i][j] == 'White':
                scoreW += add
            elif board[i][j] == 'Black':
                scoreB += add
    return scoreW - scoreB
 
# Helper func that returns list of possible moves
# Assuming AI is only white for now
def possMoves(app, board, player):
    moves = []
    if player:
        colour = 'Black'
    else:
        colour = 'White'
    for i in range(8):
        for j in range(8):
            if not board[i][j] and isMoveLegal(app, i, j, board, player):
                newBoard = copy.deepcopy(board)
                newBoard[i][j] = colour
                flipPieces(app, i, j, newBoard)
                moves.append(newBoard)
    return moves

# written the AI stuff here because its not complete, will reorganise once its working
def getScore(app, board):
    if app.ez:
        return ezScore(app, board)
    elif app.med:
        return medScore(app, board)
    elif app.hard:
        return hardScore(app, board)

# makes move for AI
def makeMove(app):
    depth = 3
    move = minimax(app, app.board, False, depth)
    print(move)
    print(app.board)
    app.board = copy.deepcopy(move[1])

# Incomplete minimax, still have to write alpha beta pruning (have written down here because its incomplete)
# Minimax alg that always runs a depth of 3, 
# diffuclty is varied by assesing board score differently
def minimax(app, board, player, depth):
    if depth == 0 or checkWin(app, board):
        return getScore(app, board), board
    # haven't accounted for the game being over
    moves = possMoves(app, board, player)
    if not player: 
        hi = None
        for move in moves:
            # New moves will be the child
            score = None
            if canSwitch(app, player, board):
                score = minimax(app, move, not player, depth-1)
            else:
                score = minimax(app, move, player, depth-1)
            if not hi or hi < score[0]:
                hi = score[0]
                goodMove = move
        return hi, goodMove
    else:
        lo = None
        for move in moves:
            # New moves will be the child
            if canSwitch(app, player, board):
                score = minimax(app, move, not player, depth-1)
            else:
                score = minimax(app, move, player, depth-1)
            if not lo or lo > score[0]:
                lo = score[0]
                goodMove = move
        return lo, goodMove

def mousePressed(app, event):
    #First checks what page is active
    if app.home:
        #checking if mouse was clicked inside a button
        if app.bx0 < event.x < app.bx1:
            if app.b1y0 < event.y < app.b1y1:
                app.home = False
                app.play = True
                playGame(app)

            #pages for other 2 buttons are not ready yet
            elif app.b2y0 < event.y < app.b2y1:
                app.home = False
                playAi(app)

            # elif app.b2y0 < event.y < app.b2y1:
            #     continue

    elif app.play:

        boardWidth = app.cols*app.size
        boardHeight = app.rows*app.size
        #Check if mouseClicked is inside a playable box
        if (app.margin < event.x < app.margin+boardWidth 
            and app.margin < event.y < app.margin + boardHeight):
            row = (event.x - app.margin)//app.size
            col = (event.y - app.margin)//app.size
            #makes move if spot is empty and legal
            if not app.board[row][col] and isMoveLegal(app, row, col, app.board, app.player):
                print(isMoveLegal(app, row, col, app.board, app.player))
                if app.player:
                    app.board[row][col] = 'Black'
                else:
                    app.board[row][col] = 'White'
                print(f'move made {row},{col}')
                #Flips all newly outflanked pieces 
                flipPieces(app, row, col, app.board) 
                #switches turn only if other player has a valid move
                if canSwitch(app, app.player, app.board):
                    print(canSwitch(app, app.player, app.board))
                    app.player = not app.player
                else: print('no switch')

                #keeps letting ai make moves until user has a legal move
                if app.Ai and not app.player:
                    while not app.player:
                        makeMove(app)
                        if canSwitch(app, app.player, app.board):
                            app.player = not app.player

                if checkWin(app, app.board): 
                    app.over = True
                    print('Game Over')
                    #game over
            else:
                print('Illegal Move')
    elif app.choose:
        #checking if mouse was clicked inside a button
        if app.bx0 < event.x < app.bx1:
            print('mmmmm')
            if app.b1y0 < event.y < app.b1y1:
                app.ez = True
                app.choose = False
                app.Ai = True
                app.play = True 
                print('tf')
            elif app.b2y0 < event.y < app.b2y1:
                app.med = True
                app.choose = False
                app.Ai = True
                app.play = True 
            elif app.b3y0 < event.y < app.b3y1:
                app.hard = True
                app.choose = False
                app.Ai = True
                app.play = True 
   

def keyPressed(app, event):
    #Going back to the home screen
    if event.key == 'Escape' and not app.home:
        app.home = True
        app.play = False
    #Restarts game
    if event.key.lower() == 'r' and app.play:
        playGame(app)

def drawHome(app, canvas):
    tx = (app.bx0 + app.bx1)//2
    ty0 = app.height/16
    fSize  = 40
    canvas.create_text(tx, ty0, text='Othello!',
                        font=f'Arial {fSize} bold')
    canvas.create_rectangle(app.bx0,app.b1y0,app.bx1,app.b1y1,
                            fill='Red', width=8)
    
    ty1 = (app.b1y0 + app.b1y1)//2
    canvas.create_text(tx, ty1, text='2 player!')
    canvas.create_rectangle(app.bx0,app.b2y0,app.bx1,app.b2y1,
                            fill='Red', width=8)
    ty2 = (app.b2y0 + app.b2y1)//2
    canvas.create_text(tx, ty2, text='Play with AI!')
    canvas.create_rectangle(app.bx0,app.b3y0,app.bx1,app.b3y1,
                            fill='Red', width=8)    
    ty3 = (app.b3y0 + app.b3y1)//2
    canvas.create_text(tx, ty3, text='"cool" feature (make your own board or smth)')                                       
    #have not decided what the 'cool' feature will be yet

    #was trying to make a button instead of just using a rectangle
    # B = tk.Button(app,
    #               text='hi')
    #               #command=printLol)             

def drawDiffuclty(app, canvas):
    tx = (app.bx0 + app.bx1)//2
    ty0 = app.height/16
    fSize  = 40
    canvas.create_rectangle(app.bx0,app.b1y0,app.bx1,app.b1y1,
                            fill='Red', width=8)
    
    ty1 = (app.b1y0 + app.b1y1)//2
    canvas.create_text(tx, ty1, text='Easy!')
    canvas.create_rectangle(app.bx0,app.b2y0,app.bx1,app.b2y1,
                            fill='Red', width=8)
    ty2 = (app.b2y0 + app.b2y1)//2
    canvas.create_text(tx, ty2, text='Medium')
    canvas.create_rectangle(app.bx0,app.b3y0,app.bx1,app.b3y1,
                            fill='Red', width=8)    
    ty3 = (app.b3y0 + app.b3y1)//2
    canvas.create_text(tx, ty3, text='Hard')   
    pass

# Helper func to get coordinates of top left 
# and bottom right coordinates of cells
def getCellBounds(app, row, col):
    x0 = app.margin + app.size*row
    y0 = app.margin + app.size*col
    x1 = x0 + app.size
    y1 = y0 + app.size
    return x0, y0, x1, y1

def drawBoard(app, canvas):
    width = app.size//10
    for i in range(len(app.board)):
        for j in range(len(app.board[0])):
            x0,y0,x1,y1 = getCellBounds(app, i,j)
            canvas.create_rectangle(x0,y0,x1,y1, fill=app.bColor,
                                    width=width)
            if app.board[i][j]:
                cWidth = ((app.size-width*2)//2)*0.2
                cx0,cy0,cx1,cy1 = x0+width, y0+width, x1-width, y1-width
                canvas.create_oval(cx0,cy0,cx1,cy1, 
                                    fill=app.board[i][j],
                                    width=cWidth)

    x = app.width//2
    y = app.margin//2
    turn = ''
    if app.player: turn = 'Black'
    else: turn = 'White'
    canvas.create_text(x,y,text=f'Turn {turn}',
                        font='Arial 16 bold')  
            
def redrawAll(app, canvas):
    if app.home:
        drawHome(app, canvas)
    elif app.play:
        drawBoard(app, canvas)
    elif app.choose:
        drawDiffuclty(app, canvas)
        
        


def runOthello():
    print('Running Othello :)')
    runApp(width=800, height=800)

def main():
    runOthello()

if (__name__ == '__main__'):
    main()





        
# Pseudo Code for the AI to play against 
# I got this from https://www.youtube.com/watch?v=l-hh51ncgDI

# function minimax(position, depth, alpha, beta, maximizingPlayer)
# 	if depth == 0 or game over in position
# 		return static evaluation of position
 
# 	if maximizingPlayer
# 		maxEval = -infinity
# 		for each child of position
# 			eval = minimax(child, depth - 1, alpha, beta false)
# 			maxEval = max(maxEval, eval)
# 			alpha = max(alpha, eval)
# 			if beta <= alpha
# 				break
# 		return maxEval
 
# 	else
# 		minEval = +infinity
# 		for each child of position
# 			eval = minimax(child, depth - 1, alpha, beta true)
# 			minEval = min(minEval, eval)
# 			beta = min(beta, eval)
# 			if beta <= alpha
# 				break
# 		return minEval
 
# // initial call
# minimax(currentPosition, 3, -∞, +∞, true)