import pyautogui as pag
import time

time.sleep(2)

topLeftX = 1417
topLeftY = 689
botRightX = 2162
botRightY = 1439

cellPixelWidth = (botRightX-topLeftX)/9
cellPixelHeight = (botRightY-topLeftY)/9

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

def findColumn(x):
    for i in range (1,10):
        if x < topLeftX + i*cellPixelWidth:
            return i-1
    return 8

def findRow(x):
    for i in range (1,10):
        if x < topLeftY + i*cellPixelHeight:
            return i-1
    return 8

for pos in pag.locateAllOnScreen("Number_icons/1.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 1

for pos in pag.locateAllOnScreen("Number_icons/2.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 2

for pos in pag.locateAllOnScreen("Number_icons/3.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 3

for pos in pag.locateAllOnScreen("Number_icons/4.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 4

for pos in pag.locateAllOnScreen("Number_icons/5.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 5

for pos in pag.locateAllOnScreen("Number_icons/6.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 6

for pos in pag.locateAllOnScreen("Number_icons/7.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 7

for pos in pag.locateAllOnScreen("Number_icons/8.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 8

for pos in pag.locateAllOnScreen("Number_icons/9.png"):
    board[findRow(pos[1])][findColumn(pos[0])] = 9  

def fillWebCells(board):
    for i in range(0,9):
        for j in range(0,9):
            pag.click(topLeftX + (i+1/2)*cellPixelWidth, topLeftY + (j+1/2)*cellPixelHeight)
            pag.press(str(board[j][i]))

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

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column tuple
    return None

def main():
    pag.click(topLeftX, topLeftY)
    print_board(board)
    solve(board)
    print("")
    print_board(board)
    fillWebCells(board)

main()
