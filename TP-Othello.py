from cmu_112_graphics import *
from scores import *
from GameFunctions import *
from math import *
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
    app.help = False
    app.choose = False
    app.hi = False
    app.custom = False
    app.set = False
    # List of all Tkinter colours. 
    # Got this from http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    # Using a set for efficiency
    app.colors = set(colors)
    createHome(app)

def createHome(app):
    app.buttonSize = app.width//10
    # coordinates for 3 main buttons
    app.bx0 = app.width//3
    app.bx1 = app.width*2//3
    app.b1y0 = app.height*4//16
    app.b1y1 = app.height*6//16
    app.b2y0 = app.b1y1 + app.height//16
    app.b2y1 = app.b2y0 + app.height*2//16
    app.b3y0 = app.b2y1 + app.height//16
    app.b3y1 = app.b3y0 + app.height*2//16

    # coordinates for extra help button
    app.hx0 = app.width*5//12
    app.hx1 = app.width*7//12
    app.hy0 = app.b3y1+ app.height//16
    app.hy1 = app.hy0 + app.height//16

    # Coordinates for leaderboard and settings buttons
    app.r = 50
    app.cx0 = app.width - app.r - 10
    app.cy0 = app.r + 10
    app.cx1 = app.r + 10

def playGame(app):
    app.board = []
    for i in range(app.rows):
        app.board += [[None]*app.rows]
    app.board[app.rows//2-1][app.cols//2-1] = app.p2Color
    app.board[app.rows//2-1][app.cols//2] = app.p1Color
    app.board[app.rows//2][app.cols//2] = app.p2Color
    app.board[app.rows//2][app.cols//2-1] = app.p1Color
    app.marginy = app.height//10
    app.size = (app.height-2*app.marginy)//app.rows
    app.marginx = (app.width-app.cols*app.size)//2
    app.player = True
    # True is black False is white
    app.over = False
    app.Ai = False 
    app.prevMove = []
    app.score = 0
    app.win = None
    app.legal = True    

def createCustom(app):
    app.message = 'Click anywhere to enter number of rows and columns'
    app.cols = 0
    app.rows = 0

def playAi(app):
    playGame(app)
    app.ez = False
    app.med = False
    app.hard = False
    app.choose = True
    app.play = False

# checks if game over and returns winner's score
def checkWin(app, board):
    for i in range(app.rows):
        for j in range(app.cols):
            if (not board[i][j] and 
                (isMoveLegal(app, i, j, board, True) or 
                isMoveLegal(app, i, j, board, False))): 
                return False
    return True
 
# Helper func that returns list of possible moves
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

# Helper function to get score of game based on difficulty
def getScore(app, board):
    if app.ez:
        return ezScore(app, board)
    elif app.med:
        return medScore(app, board)
    elif app.hard:
        return hardScore(app, board)

# makes move for AI (wrapper function for minimax)
def makeMove(app):
    # Depth for easy difficulty is 2 instead of 3
    if not app.ez:
        depth = 3
    else: depth = 2
    alpha = -200
    beta = 200
    # minimax returns best move for the AI
    move = minimax(app, app.board, alpha, beta, False, depth)
    app.board = copy.deepcopy(move[1])

# Minimax alg that always runs a depth of 3 and uses Alpha Beta Pruning, 
# diffuclty is varied by assesing board score differently
# I got the pseudocode for this from https://www.youtube.com/watch?v=l-hh51ncgDI
# (pseudocode mentioned below)
def minimax(app, board, alpha, beta, player, depth):
    if depth == 0 or checkWin(app, board):
        return getScore(app, board), board
    # haven't accounted for the game being over
    moves = possMoves(app, board, player)
    if not player: 
        hi = None
        goodMove = None
        for move in moves:
            # New moves will be the child
            score = None
            if canSwitch(app, player, move):
                score = minimax(app, move, alpha, beta, not player, depth-1)
            else:
                score = minimax(app, move, alpha, beta, player, depth-1)
            if not hi or hi < score[0]:
                hi = score[0]
                goodMove = move
            if alpha < score[0]:
                alpha = score[0]
            if beta <= alpha: break
        return hi, goodMove
    else:
        lo = None
        goodMove = None
        for move in moves:
            # New moves will be the child
            if canSwitch(app, player, move):
                score = minimax(app, move, alpha, beta, not player, depth-1)
            else:
                score = minimax(app, move, alpha, beta, player, depth-1)
            
            if not lo or lo > score[0]:
                lo = score[0]
                goodMove = move
            if beta > score[0]:
                beta = score[0]
            if beta <= alpha: break
        return lo, goodMove

def updateScore(app, score, n):
    f = open('Highscores.txt', 'r')
    scores = f.read()
    check = ''
    if app.ez:
        check = 'easy'
    elif app.med: check = 'med'
    elif app.hard: check = 'hard'
    edit = []
    makeEdit = False
    for line in scores.splitlines():
        entry = line.split()
        # Checking if either score is beaten 
        # or same score in fewer moves
        if (entry[0] == check and 
            (int(entry[1]) < score or 
            (int(entry[1]==score and entry[2]<n)))):
            edit.append([check, score, n])
            makeEdit = True
        else: edit.append(entry)
    if not makeEdit: return
    f.close()
    f = open('Highscores.txt', 'w')
    for score in edit:
        message = f'{score[0]} {score[1]} {score[2]}\n'
        f.write(message)   
    f.close()

def mousePressed(app, event):
    # First checks what page is active
    # Home Screen
    if app.home:
        #checking if mouse was clicked inside a button
        if app.bx0 < event.x < app.bx1:
            if app.b1y0 < event.y < app.b1y1:
                app.rows = 8
                app.cols = 8
                app.home = False
                app.play = True
                playGame(app)

            
            elif app.b2y0 < event.y < app.b2y1:
                app.rows = 8
                app.cols = 8
                app.home = False
                playAi(app)
            
            # page for other cool feature is not ready yet
            elif app.b3y0 < event.y < app.b3y1:
                print('yo')
                app.home = False
                createCustom(app)
                app.custom = True

        
        if ((app.hx0 < event.x < app.hx1) and
                (app.hy0 < event.y < app.hy1)):
            app.home = False
            app.help = True
        
        if (sqrt((event.x - app.cx0)**2 + (event.y - app.cy0)**2) <= app.r):
            app.hi = True
            app.home = False
        if (sqrt((event.x - app.cx1)**2 + (event.y - app.cy0)**2) <= app.r):
            app.set = True
            app.home = False

    # Custom Board Screen
    elif app.custom:
        row = col = 0
        while (not row or not col or row < 6 or 
            row > 16 or col < 6 or col > 16):
            row = app.getUserInput('Enter number of rows')
            col = app.getUserInput('Enter number of columns')
            if row and row.isdigit(): row = int(row)
            else: row = 0
            if col and col.isdigit(): col = int(col)
            else: col = 0
            if (not row or not col or row < 6 or 
                row > 16 or col < 6 or col > 16):
                app.message = 'Rows and Columns must be in between 6 and 16! Try Again'
        app.custom = False
        app.rows = int(row)
        app.cols = int(col)
        playGame(app)
        app.play = True

    # Settings Screen
    elif app.set:
        if app.bx0 < event.x < app.bx1:
            # Checks if colour is valid before changing settings
            if app.b1y0 < event.y < app.b1y1:
                colour = app.getUserInput('Enter a colour')
                if colour.lower() in app.colors:
                    app.bColor = colour
            elif app.b2y0 < event.y < app.b2y1:
                colour = app.getUserInput('Enter a colour')
                if colour.lower() in app.colors:
                    app.p1Color = colour
            elif app.b3y0 < event.y < app.b3y1:
                colour = app.getUserInput('Enter a colour')
                if colour.lower() in app.colors:
                    app.p2Color = colour

    # Game Screen
    elif app.play:
        boardWidth = app.cols*app.size
        boardHeight = app.rows*app.size
        #Check if mouseClicked is inside a playable box
        if (app.marginx < event.x < app.marginx+boardWidth 
            and app.marginy < event.y < app.marginy + boardHeight):
            row = (event.x - app.marginx)//app.size
            col = (event.y - app.marginy)//app.size
            #makes move if spot is empty and legal
            if not app.board[row][col] and isMoveLegal(app, row, col, app.board, app.player):
                app.legal = True
                prev = copy.deepcopy(app.board)
                app.prevMove.append(prev)
                if app.player:
                    app.board[row][col] = app.p1Color
                else:
                    app.board[row][col] = app.p2Color
                print(f'move made {row},{col}')
                #Flips all newly outflanked pieces 
                flipPieces(app, row, col, app.board) 
                #switches turn only if other player has a valid move
                if canSwitch(app, app.player, app.board):
                    app.player = not app.player
                else: print('no switch')

                #keeps letting ai make moves until user has a legal move
                if app.Ai and not app.player:
                    while not app.player:
                        makeMove(app)
                        if checkWin(app, app.board):
                            break
                        if canSwitch(app, app.player, app.board):
                            app.player = not app.player

                if checkWin(app, app.board): 
                    app.over = True
                    app.score = ezScore(app, app.board)
                    if app.score>0:
                        app.win = False 
                        print('white wins')
                    elif app.score<0:
                        if app.Ai:
                            print(len(app.prevMove))
                            updateScore(app, abs(app.score), 
                                        len(app.prevMove)) 
                        app.win = True
                        print('black wins')
                    else: print('draw')
                    print('Game Over')
                    #game over
            else:
                app.legal = False
                print('Illegal Move')

    # Choosing Difficulty Screen
    elif app.choose:
        #checking if mouse was clicked inside a button
        if app.bx0 < event.x < app.bx1:
            if app.b1y0 < event.y < app.b1y1:
                app.ez = True
                app.choose = False
                app.Ai = True
                app.play = True 
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
        app.help = False
        app.choose = False
        app.hi = False
        app.set = False
        app.custom

    #Restarts game
    if event.key.lower() == 'r' and app.play:
        if app.Ai: 
            playGame(app)
            playAi(app)
        else: playGame(app)
        
    #Undos previous move
    if (event.key.lower() == 'u' and app.play 
        and app.prevMove and not app.over):
        app.board = copy.deepcopy(app.prevMove[-1])
        app.prevMove.pop()
        # Won't switch player if playing 
        # against AI as user is always Black!
        if not app.Ai:
            app.player = not app.player
    if event.key.lower() == 'h':
        app.home = False
        app.hi = True
    # Test cases
    if event.key.lower() == 's' and app.play:
        app.board = [['White', 'White', 'White', 'White', 'White', 'White', 'White', 'White'],
                    ['White', 'White', 'White', 'White', 'White', 'White', 'White', None],
                    ['White', 'White', 'White', 'White', 'White', 'White', 'White', 'Black'],
                    ['White', 'White', 'White', 'White', 'White', 'White', 'White', 'White'],
                    ['White', 'White', 'White', 'White', 'White', 'Black', 'Black', 'Black'],
                    ['White', 'White', 'White', 'White', 'White', 'White', None, None],
                    ['White', 'White', 'White', 'White', 'White', None, None, None],
                    ['White', 'White', 'White', 'White', 'White', 'Black', None, None]]
    if event.key.lower() == 'e' and app.play:
        app.board = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', None],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'White'],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'White', 'White', 'White'],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'White', None, None],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'White', None, None],
                    ['Black', 'Black', 'Black', 'Black', 'Black', 'White', None, None]]

def drawHome(app, canvas):
    # Background 
    canvas.create_rectangle(0,0,app.width, app.height,
                            fill = 'Green')
    
    # Heading
    tx = app.width//2
    ty0 = app.height/16
    fSize  = 40

    canvas.create_text(tx, ty0, text='Othello!',
                        font=f'Arial {fSize} bold')
    
    #Buttons
    canvas.create_rectangle(app.bx0,app.b1y0,app.bx1,app.b1y1,
                            fill='Black', width=8)
    ty1 = (app.b1y0 + app.b1y1)//2
    canvas.create_text(tx, ty1, text='2 player',
                         font='Arial 16 bold', 
                         fill='White')
    
    canvas.create_rectangle(app.bx0,app.b2y0,app.bx1,app.b2y1,
                            fill='Black', width=8)
    ty2 = (app.b2y0 + app.b2y1)//2
    canvas.create_text(tx, ty2, text='Play with AI!', 
                        font='Arial 16 bold',
                        fill='White')
    
    canvas.create_rectangle(app.bx0,app.b3y0,app.bx1,app.b3y1,
                            fill='Black', width=8)    
    ty3 = (app.b3y0 + app.b3y1)//2
    canvas.create_text(tx, ty3, text='Custom Board',
                        font='Arial 16 bold',
                        fill='White')                                       

    canvas.create_rectangle(app.hx0, app.hy0, app.hx1, app.hy1,
                            fill='Black', width=6)
    ty4 = (app.hy0 + app.hy1)//2
    canvas.create_text(tx, ty4, text='Help?', font='Arial 12 bold',
                        fill='White')
    
    font1 = 'Arial 10 bold'
    canvas.create_oval(app.cx0-app.r, app.cy0-app.r, 
                        app.cx0+app.r, app.cy0+app.r,
                        fill='Black')
    canvas.create_text(app.cx0, app.cy0, 
                        text='Leaderboards',
                        fill='White',font=font1)
    
    canvas.create_oval(app.cx1-app.r, app.cy0-app.r, 
                        app.cx1+app.r, app.cy0+app.r,
                        fill='Black')
    canvas.create_text(app.cx1, app.cy0, 
                        text='Settings',
                        fill='White',font=font1)

def drawHelp(app, canvas):
    tx0 = app.width//2
    ty0 = app.height/16
    fSize  = 40
    canvas.create_text(tx0, ty0, text='Help',
                        font=f'Arial {fSize} bold')

    tx1 = app.width//5
    ty1 = app.height*3//16
    canvas.create_text(tx1, ty1, text='- Esc: To return to home screen',
                        font='Arial 28 bold', anchor='w' )
    
    ty2 = ty1 + 32
    canvas.create_text(tx1, ty2, text='- R: To restart game',
                        font='Arial 28 bold', anchor='w' )
    ty3 = ty2 + 32
    canvas.create_text(tx1, ty3, text='- U: To undo previous move',
                        font='Arial 28 bold', anchor='w')

def drawDiffuclty(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height,
                        fill = 'Green')
    fSize  = 30
    tx = app.width//2
    canvas.create_text(tx, app.height//8, text='Choose a difficulty to play!',
                    font=f'Arial {fSize} bold')
    ty0 = app.height/16
    fSize  = 40
    canvas.create_rectangle(app.bx0,app.b1y0,app.bx1,app.b1y1,
                            fill='Black', width=8)
    ty1 = (app.b1y0 + app.b1y1)//2
    canvas.create_text(tx, ty1, text='Easy!', font='Arial 16 bold',
                        fill='White')

    canvas.create_rectangle(app.bx0,app.b2y0,app.bx1,app.b2y1,
                            fill='Black', width=8)
    ty2 = (app.b2y0 + app.b2y1)//2
    canvas.create_text(tx, ty2, text='Medium', font='Arial 16 bold',
                        fill='White')

    canvas.create_rectangle(app.bx0,app.b3y0,app.bx1,app.b3y1,
                            fill='Black', width=8)    
    ty3 = (app.b3y0 + app.b3y1)//2
    canvas.create_text(tx, ty3, text='Hard', font='Arial 16 bold',
                        fill='White')   
    pass

def drawHighscores(app, canvas):
    tx = app.width//2
    ty0 = app.height/16
    fSize  = 40
    canvas.create_text(tx, ty0, text='Highscores!',
                        font=f'Arial {fSize} bold')
    ty1 = (app.b1y0 + app.b1y1)//2
    f = open('Highscores.txt', 'r')
    message = f.read()
    for line in message.splitlines():
        text = line.split()
        diff = ''
        if text[0] == 'easy': diff = 'Easy'
        elif text[0] == 'med': diff = 'Medium'
        elif text[0] == 'hard': diff = 'Hard' 
        canvas.create_text(tx, ty1, 
                    text=f'{diff}: {text[1]} pieces in {text[2]} moves', 
                        font='Arial 16 bold')
        ty1 += app.height//10
    f.close()

# Helper func to get coordinates of top left 
# and bottom right coordinates of cells
def getCellBounds(app, row, col):
    x0 = app.marginx + app.size*row
    y0 = app.marginy + app.size*col
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
    y = app.marginy//2
    turn = ''
    if app.player: turn = app.p1Color
    else: turn = app.p2Color
    canvas.create_text(x,y,text=f"{turn}'s turn",
                        font='Arial 16 bold')
    black = 0
    white = 0
    for row in app.board:
        black += row.count(app.p1Color)
        white += row.count(app.p2Color)
    tx0 = app.marginx//2
    tx1 = app.width - tx0
    ty0 = app.height//2 - app.size//3
    ty1 = app.height//2 + app.size//3
    if app.Ai:
        canvas.create_text(tx0,ty0,text=f"Your Score:",
                        font='Arial 18 bold')
        canvas.create_text(tx1,ty0,text=f"AI's Score:",
                        font='Arial 18 bold')
    else:
        canvas.create_text(tx0,ty0,text=f"{app.p1Color}'s Score:",
                        font='Arial 18 bold')
        canvas.create_text(tx1,ty0,text=f"{app.p2Color}'s Score:",
                        font='Arial 18 bold')
    canvas.create_text(tx0,ty1,text=f"{black}",
                        font='Arial 18 bold')
    canvas.create_text(tx1,ty1,text=f"{white}",
                        font='Arial 18 bold')
    if not app.legal:
        canvas.create_text(app.width//2,app.height-app.marginy//2,
                        text='Illegal Move :( Try again!',
                        font='Arial 18 bold',
                        fill='Red')        

    if app.over: drawWin(app, canvas)

def drawCustom(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height,
                        fill = 'Green')
    font = 'Arial 24 bold'
    canvas.create_text(app.width/2,  app.height/2,
                       text=app.message, font=font)

def drawWin(app, canvas):
    winner = ''
    if app.win != None:
        if app.win: winner = 'Black'
        else: winner = 'White'

    x0 = app.width//2 - 3*app.size
    x1 = app.width//2 + 3*app.size
    y0 = app.height//2 - app.size//1.2
    y1 = app.height//2 + app.size//1.2
    width=5
    canvas.create_rectangle(x0,y0,x1,y1, fill='White',
                            width=width)
    tx = app.width//2
    ty = app.height//2 - 35
    if winner and not app.Ai:
        canvas.create_text(tx, ty, text=f'{winner} wins by {abs(app.score)}!',
                            font='Arial 20 bold')
    elif winner and app.Ai:
        if app.win:
            canvas.create_text(tx, ty, text=f'You win by {abs(app.score)}! :)',
                                font='Arial 20 bold') 
        else:
            canvas.create_text(tx, ty, text=f'You lose by {abs(app.score)}! :(',
                                font='Arial 20 bold')
    else:
        canvas.create_text(tx, ty, text=f'Draw!', font='20 Arial bold')
    ty1 = ty + 40
    canvas.create_text(tx, ty1, 
                    text="Press 'r' to restart or",
                    font='Arial 20 bold')
    ty2 = ty1 + 40
    canvas.create_text(tx, ty2, 
                    text="'esc' to return to main Menu",
                    font='Arial 20 bold')

def drawSettings(app, canvas):
    # Background 
    canvas.create_rectangle(0,0,app.width, app.height,
                            fill = 'Green')
    
    # Heading
    tx = app.width//2
    ty0 = app.height/16
    
    #Buttons
    canvas.create_rectangle(app.bx0,app.b1y0,app.bx1,app.b1y1,
                            fill='Black', width=8)
    ty1 = (app.b1y0 + app.b1y1)//2
    canvas.create_text(tx, ty1, text='Change Board Colour',
                         font='Arial 16 bold', 
                         fill='White')
    
    canvas.create_rectangle(app.bx0,app.b2y0,app.bx1,app.b2y1,
                            fill='Black', width=8)
    ty2 = (app.b2y0 + app.b2y1)//2
    canvas.create_text(tx, ty2, text='Change Black Piece Colour', 
                        font='Arial 16 bold',
                        fill='White')
    
    canvas.create_rectangle(app.bx0,app.b3y0,app.bx1,app.b3y1,
                            fill='Black', width=8)    
    ty3 = (app.b3y0 + app.b3y1)//2
    canvas.create_text(tx, ty3, text='Change White Piece Colour',
                        font='Arial 16 bold',
                        fill='White') 

def redrawAll(app, canvas):
    if app.home:
        drawHome(app, canvas)
    elif app.help:
        drawHelp(app, canvas)
    elif app.play:
        drawBoard(app, canvas)
    elif app.choose:
        drawDiffuclty(app, canvas)
    elif app.hi:
        drawHighscores(app, canvas)
    elif app.custom:
        drawCustom(app, canvas)
    elif app.set:
        drawSettings(app, canvas)

def runOthello():
    print('Running Othello :)')
    runApp(width=1000, height=800)

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