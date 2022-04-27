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
# 7- create gameboard GUI for tow player mode.
# 8- function for deciding the moves of the system.
# 9- configure text on btn in one player mode.
# 10- create the GUI of gameboard for play along with pc.
# 11- initialize the game board to play with pc.
# 12- initialize the game board to play with another.
# 13- main function to run all the prevs functions and create the gui root.
