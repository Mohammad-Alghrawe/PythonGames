# Mohammad Alghrawe
# TecTacTeo with GUI using Tkinter
# importing all the necessary libraries.
# Tkinter GUI library.
from tkinter import *
# This module implements pseudo-random number generators.
import random
# module is for higher-order functions: functions that act on or return other functions.
from functools import partial
# This module provides generic shallow and deep copy operations.
from copy import deepcopy

# Todo list:
# 1- create an empty board. it should be global.
global board
# list 3 x 3
board = [[" " for x in range(3)] for y in range(3)]
# 2- create a variable to decide  the turn of each player.
who_is_next = 0
# 3- function to check X/O won the match or not according to the rules.
''' 
    x|x|x
    x| |
    x| |   
'''


def who_is_thewinner():
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
# 4- configure the text on btn in tow player mode.


def get_text(i, j, gb, l1, l2):
    global who_is_next
    if board[i][j] == ' ':
        if who_is_next % 2 == 0:
            # make the btn active or disabled depends on the turn.
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        who_is_next += 1
        button[i][j].config(text=board[i][j])
    if who_is_thewinner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("who_is_thewinner", "Player 1 won the match")
    elif who_is_thewinner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("who_is_thewinner", "Player 2 won the match")
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")
# 5- function to check if the place empty or not.


def isfree(i, j):
    return board[i][j] == " "
# 6- function to check the whole board.


def isfull():
    flag = True
    for i in board:
        ''' 
        The count() is a built-in function in Python. It will return the total count of a given element in a string. The counting begins from the start of the string till the end. It is also possible to specify the start and end index from where you want the search to begin.
        '''
        if(i.count(' ') > 0):
            flag = False
    return flag
# 7- create gameboard GUI for tow player mode.


def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
# 8- function for deciding the moves of the system.


def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if who_is_thewinner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]

# 9- configure text on btn in one player mode.


def get_text_pc(i, j, gb, l1, l2):
    global who_is_next
    if board[i][j] == ' ':
        if who_is_next % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        who_is_next += 1
        button[i][j].config(text=board[i][j])
    x = True
    if who_is_thewinner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("who_is_thewinner", "Player won the match")
    elif who_is_thewinner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("who_is_thewinner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):
        if who_is_next % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)

# 10- create the GUI of gameboard for play along with pc.


def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    # range(0,3) => 0,1,2
    for i in range(3):
        m = 3+i
        # append i to 3 x 3 of btns
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            ''' 
            The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget.
            '''
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
# 11- initialize the game board to play with pc.


def withpc(game_board):
    # destroy the widget. quit() stops the mainloop
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)
# 12- initialize the game board to play with another.


def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player 1 : X", width=10)

    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2 : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)
# 13- main function to run all the prevs functions and create the gui root.
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)
      
    head = Button(menu, text = "---Welcome to tic-tac-toe---",
                  activeforeground = 'red',
                  activebackground = "yellow", bg = "red", 
                  fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B1 = Button(menu, text = "Single Player", command = wpc, 
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B2 = Button(menu, text = "Multi Player", command = wpl, activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 500, font = 'summer', bd = 5)
      
    B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 500, font = 'summer', bd = 5)
    head.pack(side = 'top')
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()
