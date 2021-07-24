"""
Tic Tac Toe Player
"""

import math

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


def test_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if(board == initial_state()):
        print("Empty Board, X's turn")
        return X
    x = []
    o = []
    for i in board:
        for j in i:
            if j == X:
                x.append(X)
            if j == O:
                o.append(O)

    if len(x) > len(o):
        print("O's turn")
        return O
    if len(x) < len(o):
        print("x's turn")
        return X
    if len(x) == len(o):
        print("X's turn")
        return X        

    print (x)
    print(o)
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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
