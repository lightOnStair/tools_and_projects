# Jiangxiao Xie xiexx647

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work. None of it was
# obtained from any source other than material presented as part of the
# course
import turtle
import math
import random
turtle.delay(0)
turtle.setworldcoordinates(-100,800,800,-100)
def initialBoardGraph():
    '''creat an enmpty board graph'''
    turtle.setworldcoordinates(-100,800,800,-100)
    turtle.color("lightgreen")
    turtle.shape("square")
    turtle.shapesize(4,4,1)
    turtle.penup()
    turtle.hideturtle()
    for i in range(8):
        if i % 2 == 0:
            for j in range(0,8,2): #the corlors of the cells alternate betwwen green and lightgreen
                turtle.setpos(i*100,j*100)
                turtle.stamp()
        else:
            for j in range(1,8,2):
                    turtle.setpos(i*100,j*100)
                    turtle.stamp()
    turtle.color("green")
    for i in range(8):
        if i % 2 == 0:
            for j in range(1,8,2):
                    turtle.setpos(i*100,j*100)
                    turtle.stamp()
        else:
            for j in range(0,8,2):
                turtle.setpos(i*100,j*100)
                turtle.stamp()
    for i in range(8): # indicate row and column number on the graph
        turtle.setpos(-100,i*100+50)
        turtle.write(i,font = ("Arial", 50, "normal"))
    for i in range(8):
        turtle.setpos(i*100,-40)
        turtle.write(i,font = ("Arial", 50, "normal"))


def surrondCells(row,col):
    '''find all adjacent cells of a specific cell'''
    surrond = []
    # for the upperleft cell
    if row == 0 and col ==0:
        for i in range(row,row+2):
            for j in range(col,col+2):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for the upperright cell
    elif row == 0 and col ==7:
        for i in range(row,row+2):
            for j in range(col-1,col+1):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for the lowerleft cell
    elif row == 7 and col == 0:
        for i in range(row-1,row+1):
            for j in range(col,col+2):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for the lowerright cell
    elif row == 7 and col == 7:
        for i in range(row-1,row+1):
            for j in range(col-1,col+1):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for cell 01 to 06
    elif row == 0:
        for i in range(row,row+2):
            for j in range(col-1,col+2):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for cell 71 to 76
    elif row == 7:
        for i in range(row-1,row+1):
            for j in range(col-1,col+2):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for cell 10 to 60
    elif col == 0:
        for i in range(row-1,row+2):
            for j in range(col,col+2):
                if i != row or j != col:
                    surrond += [(i,j)]
    # for cell 17 to 67
    elif col == 7:
        for i in range(row-1,row+2):
            for j in range(col-1,col+1):
                if i != row or j != col:
                    surrond += [(i,j)]
    # other cells
    else:
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i != row or j != col:
                    surrond += [(i,j)]
    return surrond


def isValidMove(board,row,col,color):
    '''judge if a move of a token of one color is legal'''
    if board[row][col] != 0:
        return False
    else:
        surrond = surrondCells(row,col)
        for cell in surrond:
            i = cell[0]
            j = cell[1]
            if board[i][j] != 0 and board[i][j] != color:
                # if the token belongs to the other color:
                newrow = i
                newcol = j
                delrow = row - i
                delcol = col - j
                while newrow<=7 and newrow>=0 and newcol <=7 and newcol>=0:
                    if board[newrow][newcol] == 0:
                        # if the next cell is empty, it's not valid.
                        break
                    if board[newrow][newcol] == color:
                        # if the next token belongs to the player, it's valid.
                        return True
                    else:
                        # if the next cell still belongs to the other player,
                        # continue to see next cell.
                        newrow -= delrow
                        newcol -= delcol
        return False


def flip(board,row,col,color):
    '''flip tokens after one move'''
    board[row][col] = color
    surrond = surrondCells(row,col)
    totalCellsNeedFlip = []
    for cell in surrond:
        i = cell[0]
        j = cell[1]
        if board[i][j] != 0 and board[i][j] != color:
            # if the cell belongs to the other player.
            delrow = row - i
            delcol = col - j
            count = 0
            while True:
                i -= delrow
                j -= delcol
                count += 1   # count numbers of tokens that need to be flipped.
                if i<0 or i>7 or j<0 or j >7:
                    # if the next cell is out of the board:
                    break
                if board[i][j] == 0:
                    # if the next cell is empty
                    break
                if board[i][j] == color:
                    # if the next cell belongs to the player:
                    for k in range(count):
                        i += delrow
                        j += delcol
                        totalCellsNeedFlip += [(i,j)]
                        # record every token that needs to be flipped here.
                    break

    for cell in totalCellsNeedFlip:
        #flip
        if board[cell[0]][cell[1]] == "black":
            board[cell[0]][cell[1]] = "white"
        else:
            board[cell[0]][cell[1]] = "black"
    return board



def terminateGame(board):
    '''judge if game is over'''
    if getValidMove(board,"black") + getValidMove(board,"white") == []:
        return 0

def findwinner(board):
    '''if the game is over, see who wins'''
    turtle.penup()
    blackCount,whiteCount = 0,0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "black":
                blackCount += 1
            elif board[i][j] == "white":
                whiteCount += 1
    turtle.setpos(350,780)
    if blackCount > whiteCount:
        turtle.write("congratulation! you win!",move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(blackCount,move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(":    ",align="center",font=("Arial",20,"normal"))
        turtle.write(whiteCount,move = True,align="center",font=("Arial",20,"normal"))
    elif blackCount == whiteCount:
        turtle.write("good game, draw",move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(blackCount,move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(":    ",align="center",font=("Arial",20,"normal"))
        turtle.write(whiteCount,move = True,align="center",font=("Arial",20,"normal"))
    elif blackCount < whiteCount:
        turtle.write("AI wins, he's good",move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(blackCount,move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(":    ",move=True,align="center",font=("Arial",20,"normal"))
        turtle.write(whiteCount,move = True,align="center",font=("Arial",20,"normal"))



def getValidMove(board,color):
    '''find all valid moves of one color'''
    allValidMove = []
    for row in range(8):
        for col in range(8):
            if isValidMove(board,row,col,color) == True:
                allValidMove += [(row,col)]
    return allValidMove


def initialBoardList():
    '''the initial status of a game, in list'''
    board = []
    rowlist = []
    for i in range(8):
        rowlist += [0]
        board += [0]
    for i in range(8):
        board[i] = rowlist.copy()
    board[3][3] = "white"
    board[3][4] = "black"
    board[4][3] = "black"
    board[4][4] = "white"
    return board


def singlemove(col,row,color):
    '''put one move in graph'''
    turtle.hideturtle()
    turtle.penup()
    turtle.setworldcoordinates(-100,800,800,-100)
    turtle.shape("circle")
    turtle.shapesize(4)

    turtle.color(color)
    turtle.setpos(row*100,col*100)
    turtle.stamp()
    turtle.home()


def player(board,location):
    '''receive a string that indicates where to move and do flips'''
    row = int(location[0])
    col = int(location[1])
    board[row][col] = "black"
    flip(board,row,col,"black")
    return board


def boardmove(board):
    '''show board in graph'''
    for i in range(8):
        for j in range(8):
            if board[i][j] == "black":
                singlemove(i,j,"black")
            if board[i][j] == "white":
                singlemove(i,j,"white")


def selectNextPlay(board):
    '''AI plays'''
    choPairList = getValidMove(board,"white")
    if choPairList != []:
        # let AI randomly pick a move
        getCellIndex = random.randint(0,len(choPairList)-1)
        row,col = choPairList[getCellIndex][0], choPairList[getCellIndex][1]
        board[row][col] = "white"
        return flip(board,row,col,"white")
    else:
        print("no valid moves for AI")
        return board


def main():
    initialBoardGraph()
    board = initialBoardList()
    boardmove(board)
    while True:
        location = turtle.textinput("othello","input row and col, do not split(e.g. 23)")
        choPairList = getValidMove(board,"black")
        if location == "":
            return "game terminated"
        row = int(location[0])
        col = int(location[1])
        if choPairList == []:
            print("no valid moves for you")
            '''attention: even if you find you don't have any valid location
               you still need to input a cell to jump your turn'''
            a = selectNextPlay(board)
            boardmove(board)
            if terminateGame(board) == 0:
                break
        elif (row,col) not in choPairList:
            print("this is not a valid move")
            True
        else:
            board = player(board,location)
            boardmove(board)
            if terminateGame(board) == 0:
                break
            a = selectNextPlay(board)
            boardmove(board)
            if terminateGame(board) == 0:
                break
    findwinner(board)
    return

if __name__ == '__main__':
    main()
