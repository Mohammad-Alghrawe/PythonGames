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
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            # make the btn active or disabled depends on the turn.
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
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

# 9- configure text on btn in one player mode.
# 10- create the GUI of gameboard for play along with pc.
# 11- initialize the game board to play with pc.
# 12- initialize the game board to play with another.
# 13- main function to run all the prevs functions and create the gui root.
