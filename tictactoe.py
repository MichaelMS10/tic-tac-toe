"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
TURN = X
WINNER = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    """return [[X, O, X],
            [O, O, X],
            [O, X, O]]"""
 
    """return [[EMPTY, X, O],
            [O, X, EMPTY],
            [X, EMPTY, O]]"""
    
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

    if (X_count == 0 and O_count == 0) or (X_count <= O_count):
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

    "Raise an exception if action is not valid"
    if not action:
        return board
    
    try:
        i, j = action
        i = int(i)
        j = int(j)
    except ValueError:
        raise ValueError("Invalid action: row and column should be integers")
    
    "Iterate over the board and input the action performed"
    for i in range(3):
        for j in range(3):
            if action == (i, j):
                copied_board[i][j] = player(board)
            
    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    WINNER = None

    "Verify if X is winner"

    if (board[0][0] == X and board[0][1] == X and board[0][2] ==X) or (board[1][0] == X and board[1][1] == X and board[1][2] ==X) or (board[2][0] == X and board[2][1] == X and board[2][2] ==X):
        WINNER = X
    elif (board[0][0] == X and board[1][0] == X and board[2][0] ==X) or (board[0][1] == X and board[1][1] == X and board[2][1] ==X) or (board[0][2] == X and board[1][2] == X and board[2][2] ==X):
        WINNER = X
    elif (board[0][0] == X and board[1][1] == X and board[2][2] ==X) or (board[2][0] == X and board[1][1] == X and board[0][2] ==X):
        WINNER = X

    "Verify if O is winner"
    if (board[0][0] == O and board[0][1] == O and board[0][2] == O) or (board[1][0] == O and board[1][1] == O and board[1][2] == O) or (board[2][0] == O and board[2][1] == O and board[2][2] == O):
        WINNER = O
    elif (board[0][0] == O and board[1][0] == O and board[2][0] == O) or (board[0][1] == O and board[1][1] == O and board[2][1] == O) or (board[0][2] == O and board[1][2] == O and board[2][2] == O):
        WINNER = O
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[2][0] == O and board[1][1] == O and board[0][2] == O):
        WINNER = O

    return WINNER


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    is_terminal = False
    empty_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_count +=1

    if (winner(board) != None) or (empty_count == 0):
        is_terminal = True

    return is_terminal


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    WINNER = winner(board)

    utility_value = 0

    if WINNER == X:
        utility_value = 1

    elif WINNER == O:
        utility_value = -1

    return utility_value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        best_move = None
    
    moves = actions(board) 
    moves_utilities = []
    current_player = player(board)
    best_move = None
    boards = {}

    if current_player == X:
        # Iterate over moves and calculate their utilities
        for move in moves:
            new_board = result(board, move)
            utility_value = min_value(new_board) 
            moves_utilities.append((move, utility_value))
        
        # Find the move with the maximum utility value
        best_move = max(moves_utilities, key=lambda x: x[1])[0]        

    elif current_player == O:
        # Iterate over moves and calculate their utilities
        for move in moves:
            new_board = result(board, move)
            utility_value = max_value(new_board)
            moves_utilities.append((move, utility_value))

        # Find the move with the minimum utility value
        best_move = min(moves_utilities, key=lambda x: x[1])[0]      

    return best_move

def max_value(board):
    """
    Returns the maximum utility value for the current player.
    """
    if terminal(board):
        v = utility(board) 

    else:
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))

    return v

def  min_value(board):
    """
    Returns the minimum utility value for the current player.
    """
    if terminal(board):
        v = utility(board)

    else:
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))

    return v