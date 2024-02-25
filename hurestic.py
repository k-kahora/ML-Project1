
from typing import DefaultDict, Set

from tic_tac_toe import calculate_position


def evaluate_board(board, symbol):
    """
    Evaluate the current state of the board
    board: 2D list representing the tic-tac-toe board
    symbol: Symbol of the opponent 
    """
    winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    if symbol == 'X':
        opponent_symbol = 'O'
    else:
        opponent_symbol = 'X'

    score = 0
    # Check rows, columns, and diagonals for two-in-a-rows
    marked = set()
    directions = [(-1,0),(1,0),(1,1),(-1,-1),(0,1),(0,-1),(1,-1),(-1,1)]
    for i in range(1,10):
    # Add to score for each two-in-a-row with the opponent's symbol
        row,col = calculate_position(i)
        for r,c in directions:
            row_m, col_m = row + r, col + c
            if (row_m > 2 or row_m < 0 or col_m < 0 or col_m > 2 or board[row][col] != opponent_symbol or (row_m,col_m) in marked):
                print(row_m,col_m)
                continue
            print("victory")
            if (board[row_m][col_m] == board[row][col]):
                marked.add((row,col))
                score += 1



    # Subtract from score for each two-in-a-row with your symbol
    # Implement your scoring logic here

    print(marked)
    return score


def choose_best_move(board, symbol):
    """
    Choose the best move for the current board state not looking into the future
    board: 2D list representing the tic-tac-toe board
    symbol: Symbol of the opponent 
    """
    best_score = -float('inf') # Initialize it to the worst score possible
    best_move = None
    for i in range(3):  
        for j in range(3):
            if board[i][j] == ' ':  
                board[i][j] = symbol  
                score = evaluate_board(board, symbol) # Set the score of the curent move
                board[i][j] = ' '  # Undo the temporary move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

test_board = [['O', 'O', None ], [None, 'O', None], [None, None, None], ]
print("Eval:",evaluate_board(test_board,'X'))
