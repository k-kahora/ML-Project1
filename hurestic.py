
from typing import DefaultDict, Set

from tic_tac_toe import calculate_position


def evaluate_board(board, symbol):
    """
    Evaluate the current state of the board
    board: 2D list representing the tic-tac-toe board
    symbol: Symbol of the opponent 
    example:[['O', 'O', 'X' ], ['X', 'O', None], ['X', None, None], ] should return 3 as there is 3 places where O has two in a row
    """

    winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    if symbol == 'X':
        opponent_symbol = 'O'
    else:
        opponent_symbol = 'X'
        
    opp_score = 0
    score = 0
    
        
    for combo in winning_combos:
        symbols = [board[row][col] for pos in combo for row, col in [calculate_position(pos)]]
        print(symbols)
        if symbols.count(opponent_symbol) == 2 and symbols.count(None) == 1:
            opp_score += 1
        elif symbols.count(symbol) == 2 and symbols.count(None) == 1:
            score += 1  

    return score - opp_score


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
            if board[i][j] == None:  
                board[i][j] = symbol  
                score = evaluate_board(board, symbol) # Set the score of the curent move
                board[i][j] = None  # Undo the temporary move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

test_board = [['O', 'O', None ], [None, 'O', 'X'], [None, None, 'X'], ]
print("Eval:",evaluate_board(test_board,'X'))
print("Best Move:",choose_best_move(test_board,'X'))
print(test_board)

def opponent_turn(board, symbol):
    """
    Perform the opponent's turn.
    """
    i, j = choose_best_move(board, symbol)
    if i is not None and j is not None:
        board[i][j] = symbol
        return True  # Move was made
    return False  # No move made (board is full)
