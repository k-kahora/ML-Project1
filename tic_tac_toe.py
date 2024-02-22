# tic_tac_toe.py


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
        pass
    
    def play_game(self):
        # Main game loop
        xTurn = False
        while True:
            user_input = int(input("Enter a board number to play"))
            if user_input < 1 or user_input > 9:
                print("Not a valid input")
                continue
            row = (user_input - 1) // 3
            col = (user_input - 1) % 3

            self.board[row][col] = 'X' if xTurn else 'O' 
            xTurn = not xTurn
            self.print_board()
        pass
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

if __name__ == "__main__":
    # Command line interface to run the game
    x = TicTacToe()
    x.print_board()
    x.play_game()
    pass
