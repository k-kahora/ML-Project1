# tic_tac_toe.py

def calculate_position(pos):
    return (pos - 1) // 3, (pos - 1) % 3

class TicTacToe:
    def __init__(self):
        # Initialize the board, players, etc.
        self.board = [[None, None, None ], [None, None, None], [None, None, None], ]
        self.positions = """
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
"""
    def reset_board(self):
        self.board = [[None, None, None ], [None, None, None], [None, None, None], ]
    
    def calculate_winner(self):
        lines = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for row in lines:
            a,b,c = [calculate_position(pos) for pos in row]
            a_row, a_col = a
            b_row, b_col = b
            c_row, c_col = c
            if (self.board[a_row][a_col] and self.board[a_row][a_col] == self.board[b_row][b_col] and self.board[a_row][a_col] == self.board[c_row][c_col]):
                return self.board[a_row][a_col]
        return None

		# if (self.board[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
		# 	return squares[a];
		# }

    
    def play_game(self):
        # Main game loop
        xTurn = False
        while True:
            user_input = int(input("Enter a board number to play"))
            row,col = calculate_position(user_input)
            if (row < 0 or row > 2 or col < 0 or col > 2 or self.board[row][col] != None):
                print("Not a valid input")
                continue
            self.board[row][col] = 'X' if xTurn else 'O' 
            winner = self.calculate_winner()
            # Check for draw
            draw = all(all(col is not None for col in row) for row in self.board)
            if (draw):
                print('Draw')
                return "draw"
            # Check for winner
            if (winner):
                return "win" if winner == 'X' else 'loss'
            xTurn = not xTurn
            self.print_board()
    def print_board(self):
        print(self.positions)
        for row in self.board:
            row_ = list(map(lambda a: ' ' if a == None else a,row))
            print("|{0}|{1}|{2}|".format(row_[0], row_[1], row_[2]))

class AIPlayer:
    def __init__(self, learning=False):
        # Initialize AI player, with optional learning capability
        pass
    
    def choose_move(self, board):
        # Implement move choice logic here
        pass
# Other necessary classes/functions...

def play_game():
    x = TicTacToe()
    x.print_board()
    print(x.play_game())
    x.reset_board()

if __name__ == "__main__":
    # Command line interface to run the game
    x = TicTacToe()
    x.print_board()
    x.play_game()
    pass
