"""
Tic Tac Toe Player
"""
# This is the solution file that I tested

import math
import random
from copy import deepcopy


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
    # Scan board for entries and determine next player:

    X_count = 0
    O_count = 0
    EMPTY_count = 0

    for row in board:
      X_count += row.count(X)
      O_count += row.count(O)
      EMPTY_count += row.count(EMPTY)

    # If X has more squares than O, its O's turn:
    if X_count > O_count:
      return O
    # Otherwise it is X's turn:
    else:
      return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i represents the board row, j the board column, both 0, 1 or 2
    The actions are are represented as the tuple (i, j) where the piece can be placed.
    """
    possible_moves = set()
    
    for rows_idx in range(len(board)):
       for column_idx in range(len(board[rows_idx])):
          if board[rows_idx][column_idx] == EMPTY:
             possible_moves.add((rows_idx, column_idx))
    return possible_moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    # Check move is valid:
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
      raise ValueError(action, board, 'Result function given an invalid board position for action: ')
    elif board[i][j] != EMPTY:
      raise ValueError(action, board, 'Result function tried to perform invalid action on occupaied tile: ')

    # Make a deep copy of the board and update with the current player's move:
    board_copy = deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
  """
  Returns the winner of the game, if there is one.
  otherwise return None
  """
  # Check rows:
  for row in board:
    if row == [X, X, X]:
      return X
    elif row == [O, O, O]:
      return O    

  # Check columns:
  if board[0][0] == O and board[1][0] == O and board[2][0] == O:
    return O
  elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
    return O
  elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
    return O
  
  if board[0][0] == X and board[1][0] == X and board[2][0] == X:
    return X
  elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
    return X
  elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
    return X

  # Check Diagonals:
  if board[0][0] == O and board[1][1] == O and board[2][2] == O:
    return O
  elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
    return O
  
  if board[0][0] == X and board[1][1] == X and board[2][2] == X:
    return X
  elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
    return X

  # Otherwise no current winner, return None
  return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """ 
    # Game is over if it is a winning board or all tiles are full (no actions):

    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == 'X':
      return 1
    elif winner(board) == 'O':
      return -1
    else:
      return 0

actions_explored = 0


def minimax(board):
  """
  Returns the optimal action for the current player on the board.
  'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
  """
  return minimax_helper(board)[1]

def minimax_helper(board):
    """
    Recursive helper function to find the optimal action.
    """
    # Base case: if the game is over, return the utility value and no action.
    if terminal(board):
        return utility(board), None

    # Maximize for X
    if player(board) == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            ret_value, _ = minimax_helper(result(board, action))
            if ret_value > best_value:
                best_value = ret_value
                best_action = action
        return best_value, best_action

    # Minimize for O
    else:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            ret_value, _ = minimax_helper(result(board, action))
            if ret_value < best_value:
                best_value = ret_value
                best_action = action
        return best_value, best_action