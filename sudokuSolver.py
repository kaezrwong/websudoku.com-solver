import pyautogui as pag
import time

# Allow time to switch to sudoku browser window
time.sleep(2)

# Pixel locations of top left and bottom right vertices
# of the sudoku. Found using findPixelBounds.py
topLeftX = 1418
topLeftY = 642
botRightX = 2159
botRightY = 1388

# Calculations for widths and heights of individual
# sudoku cells.
cellPixelWidth = (botRightX-topLeftX)/9
cellPixelHeight = (botRightY-topLeftY)/9

# Clears the internal sudoku board
def clearBoard(board):
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    return board

# Given an x coordinate, returns the corresponding
# column index in internal sudoku board
def findColumn(x):
    for i in range (1,10):
        if x < topLeftX + i*cellPixelWidth:
            return i-1
    return 8

# Given a y coordinate, returns the corresponding
# row index in internal sudoku board
def findRow(y):
    for i in range (1,10):
        if y < topLeftY + i*cellPixelHeight:
            return i-1
    return 8

# Finds the button to generate a new sudoku and clicks it
def newSudoku():
    pos = None
    while pos == None:
        pos = pag.locateOnScreen("Button_icons/newPuzzle.png")
        if pos == None:
            pos = pag.locateOnScreen("Button_icons/newPuzzle2.png")
    pag.click(pos)

    return 0

# Finds the button to finish sudoku and clicks it
def finishSudoku():
    pos = pag.locateCenterOnScreen("Button_icons/finishPuzzle.png")
    pag.click(pos)
    return 0

# Reads in sudoku board from web browser and fills
# in internal sudoku board
def readInSudoku(board):
    # Check if page is loaded
    while (pag.locateOnScreen("Number_icons/1.png") == None):
        if pag.locateOnScreen("Number_icons/2.png") != None:
            break
        time.sleep(0.1)

    for i in range (1, 10):
        for pos in pag.locateAllOnScreen("Number_icons/"+str(i)+".png"):
            board[findRow(pos[1])][findColumn(pos[0])] = i
    return board

# Fills sudoku board from web browser with values
# from internal sudoku board
def fillWebCells(board):
    for i in range(0,9):
        for j in range(0,9):
            pag.click(topLeftX + (i+1/2)*cellPixelWidth, topLeftY + (j+1/2)*cellPixelHeight)
            pag.press(str(board[j][i]))

# Solves internal sudoku board via backtracking
def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True
            
            board[row][column] = 0
    
    return False

# Given a sudoku board, valid places a number (1-9)
# at a position in the board and returns whether it
# is valid (no contradictions in the row, column or
# 3x3 box)
def valid(board, number, position):

    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    
    return True

# Prints the internal sudoku board to console
def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else: 
                print(str(board[i][j]) + " ", end="")

# Find an empty cell in the internal sudoku board
# and returns the array index as a tuple
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column tuple
    return None

def main():
    # Initalise empty internal sudoku board.
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    
    for it in range(1,100):
        readInSudoku(board)
        pag.click(topLeftX, topLeftY)
        print_board(board)
        solve(board)
        print("")
        print('Solved')
        print_board(board)
        print("")
        fillWebCells(board)
        finishSudoku()
        time.sleep(2)
        newSudoku()
        board = clearBoard(board)
        pag.click(botRightX, botRightY)


main()

2
