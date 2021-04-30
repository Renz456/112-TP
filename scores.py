# Heuristics for assessing board value
# Assumes AI is always white

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

# Corners and edges weighted more, 10 for corners 3 for edge
# adjacents to opposite corners weighted as negative
def hardScore(app, board):
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
                        and board[0][0] == opponent):
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