import numpy as np
import matplotlib.pyplot as plt
import random

class TicTacToeAI:
    def __init__(self):
        # initialize weights used for board evaluation: 1. Bias term, 2. Presence of 1 'X', 3. presence of 2 'X's
        #4. Presence of 1 'O', 5. Presence of 2 'O's
        self.weights = np.random.rand(5)#weights initialized to a rand value
        self.alpha = 0.1  # learning rate for weight updates

    def extract_features(self, board):
        # Extract features from the board to use in evaluation
        features = np.zeros(5)# Initialize feature vector
        features[0] = 1  # bias term
        lines = self._get_lines(board)# Get all possible lines (rows, columns, diagonals)

        for line in lines:
        # Count occurrences of 'X' and 'O' in each line to set other feature values
            x_count = line.count('X')
            o_count = line.count('O')
            if x_count == 1 and o_count == 0:
                features[1] += 1# One 'X'
            elif x_count == 2 and o_count == 0:
                features[2] += 1# Two 'X's
            elif x_count == 0 and o_count == 1:
                features[3] += 1# One 'O'
            elif x_count == 0 and o_count == 2:
                features[4] += 1# Two 'O's
        return features

    def evaluate_board(self, board):
        # Evaluate the current board using the model's weights
        features = self.extract_features(board)
        #returns dot product, which represents the combination of features and weights into a single value
        #this represents the overall AI's evaluation of the board, high score=more favorable board state, low score=less favorable board state
        return np.dot(self.weights, features)

    def _get_lines(self, board):#gets all possible lines from the board
        lines = []
        # rows and columns
        for i in range(3):
            lines.append([board[i][j] for j in range(3)])  # rows
            lines.append([board[j][i] for j in range(3)])  # columns
        # diagonals
        lines.append([board[i][i] for i in range(3)])
        lines.append([board[i][2-i] for i in range(3)])
        return lines

    def update_weights(self, board, outcome):#updates weights based on game outcome, learning takes place here
        # Update model weights based on the outcome of a game
        target = 1 if outcome == 'win' else 0 if outcome == 'loss' else 0.5
        prediction = self.evaluate_board(board)
        error = target - prediction# Calculate error, which represents how far off the AI's eval was to the outcome
        features = self.extract_features(board)#features extracted to get the board condition that led tho the outcome
        self.weights += self.alpha * error * features# Update weights with weight adjustment formula

class TicTacToeGame:
    def __init__(self, ai):
        self.board = [['' for _ in range(3)] for _ in range(3)]# Initialize empty board
        self.ai = ai# AI player
        self.opponent = 'O'# Opponent's marker
        self.ai_player = 'X'# AI's marker

    def play_game(self, learn=True):
        # Main game loop
        turn = 'X'# Start with 'X', assuming 'X' is the AI player
        while True:
            if turn == self.ai_player:
                self.ai_move()# AI makes a move
            else:
                self.random_move()# Opponent makes a random move
            winner = self.check_winner()# Check for a winner
            if winner or self.is_board_full():
                # If there's a winner or the board is full, the game ends
                # If learning is enabled, update the AI's weights based on game outcome
                if learn and winner == self.ai_player:
                    self.ai.update_weights(self.board, 'win')
                elif learn and winner == self.opponent:
                    self.ai.update_weights(self.board, 'loss')
                elif learn and winner is None:# No winner means a draw
                    self.ai.update_weights(self.board, 'draw')
                return winner# Return the winner ('X', 'O', or None for a draw)
            turn = self.opponent if turn == self.ai_player else self.ai_player# Switch turns

    def ai_move(self):
        # AI calculates the best move based on the current board state
        best_score = -np.inf# Initialize best score to negative infinity for comparison
        best_move = None# Initialize best move
        for i in range(3):# Iterate through rows and columns
            for j in range(3):
                if self.board[i][j] == '':# Reset the board
                    self.board[i][j] = self.ai_player# Temporarily make the move
                    score = self.ai.evaluate_board(self.board)# Evaluate the board with the move
                    self.board[i][j] = ''# Undo the move
                    if score > best_score:# If this move is better than previous best, update to find the best move based on the highest eval score
                        best_score = score
                        best_move = (i, j)
        if best_move:
            self.board[best_move[0]][best_move[1]] = self.ai_player# Make the best move

    def random_move(self):# Opponent makes a random valid move
        moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']
        if moves:# If there are available spots
            move = random.choice(moves)# Choose a random move
            self.board[move[0]][move[1]] = self.opponent# Make the move

    def check_winner(self):# Check if there's a winner
        lines = self.ai._get_lines(self.board)# Get all lines (rows, columns, diagonals)
        for line in lines:# Check each line for a win condition
            if line == ['X', 'X', 'X']:
                return 'X'#ai wins
            elif line == ['O', 'O', 'O']:# Opponent wins
                return 'O'
        return None# No winner yet

    def is_board_full(self):
        # Check if the board is full (no empty spaces)
        for row in self.board:
            if '' in row:
                return False# Board is not full
        return True# Board is full

def train_and_evaluate(games=10000):
    # Function to train the AI and evaluate its performance
    ai = TicTacToeAI()
    results = {'win': 0, 'loss': 0, 'draw': 0}# Initialize results
    for _ in range(games):# Play the specified number of games
        game = TicTacToeGame(ai)
        result = game.play_game()# Play a game
        if result == 'X':# Increment the result counters based on the outcome
            results['win'] += 1
        elif result == 'O':
            results['loss'] += 1
        else:
            results['draw'] += 1

    # Plotting results
    labels = list(results.keys())
    values = [results[label] / games * 100 for label in labels]
    plt.bar(labels, values)
    plt.ylabel('% of Games')
    plt.title('AI Performance Over {} Games'.format(games))
    plt.savefig('ai_performance_over_{}_games.png'.format(games))
    #output final results
    print("Training completed. The AI won {win} games, lost {loss} games, and drew {draw} games.".format(**results))


if __name__ == "__main__":
    print("here")
    train_and_evaluate()


