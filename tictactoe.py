"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

 
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    "Iterate over the board and count X and O"
    X_count = 0
    O_count = 0

    turn = X

    for row in board:
        for cell in row:
            if cell == X:
                X_count += 1
            elif cell == O:
                O_count += 1

    if (X_count == 0 and O_count == 0) or X_count > O_count:
        turn = X
    else:
        turn = O   
    
    return turn


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    "Iterate over the board and return a set of all possible actions"
    possible_actions = []

    i = -1
    j = -1

    for row in board:
        i += 1
        for cell in row:
            if j >= 2:
                j = -1
            j += 1
            if cell == EMPTY:
                possible_actions.append((i, j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    "Create a deep copy of the board"
    copied_board = copy.deepcopy(board)
    
    "Iterate over the board and input the action performed"
    for i in range(3):
        for j in range(3):
            if action == (i, j):
                copied_board[i][j] = action 
            
    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
