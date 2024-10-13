def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i represents the board row, j the board column, both 0, 1 or 2
    The actions are are represented as the tuple (i, j) where the piece can be placed.
    """
    possible_moves = set()
    
    for rows_idx in range(len(board)):
       for column_idx in range(len(board[rows_idx])):
          if board[rows_idx][column_idx] is EMPTY:
             possible_moves.add((rows_idx, column_idx))
    return possible_moves


X = "X"
O = "O"
EMPTY = None
board = [[X, EMPTY, EMPTY],
[EMPTY, O, EMPTY],
[EMPTY, EMPTY, EMPTY]]

print(actions(board))