# Machin Learining.py
# Step 1: Define board featureschoose_best_move
from hurestic import choose_best_move
import tic_tac_toe_ai
from tic_tac_toe_ai import calculate_position


def choose_move(board, weights):
    best_score = -float("inf")
    best_move = None

    for pos in range(1, 10):  # Assuming board is a flat list of 9 elements
        i, j = calculate_position(pos)
        if board[i][j] is None:  # Check if the position is empty
            board[i][j] = "X"  # Temporarily make the move
            score = evaluate_board(board, weights)
            board[i][j] = None  # Undo the move

            if score > best_score:
                best_score = score
                best_move = pos

    return best_move


def compute_features(board):
    # Example features:
    # - Number of rows, columns, diagonals with 2 'X' and 1 empty space
    # - Number of rows, columns, diagonals with 2 'O' and 1 empty space
    # - ...
    features = [
        0,  # - Number of rows, columns, diagonals with 2 'X' and 1 empty space
        0,  # - Number of rows, columns, diagonals with 2 'O' and 1 empty space
        0,  # - Center control
        0,  # - Winning moves available
    ]  # [winning_opportunities_for_X, block_opportunities_against_O]
    winning_lines = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]

    for line in winning_lines:
        symbols = [
            board[row][col] for pos in line for row, col in [calculate_position(pos)]
        ]
        X_count = symbols.count("X")
        O_count = symbols.count("O")
        Empty_count = symbols.count(None)

        if X_count == 2 and Empty_count == 1:
            features[0] += 1
        if X_count == 3:
            features[3] = 1
        if O_count == 2 and Empty_count == 1:
            features[1] += 1
    features[2] = 1 if board[1][1] == "X" else 0

    return features


# Step 2: Create the initial evaluation function
def evaluate_board(board, weights):
    features = compute_features(board)
    value = sum(weight * feature for weight, feature in zip(weights, features))
    return value


def initialize_weights():
    return [0.1, 0.1, 0.1, 1]


def initialize_board():
    return tic_tac_toe_ai.TicTacToeAi()


# Step 3: Learning algorithm to update weights
def update_weights(weights, outcome, learning_rate):
    # Adjust weights based on the outcome of a game
    # This is a simplified version; actual implementation may vary
    if outcome == "win":
        weights = [w + learning_rate for w in weights]
    elif outcome == "loss":
        weights = [w - learning_rate for w in weights]
    # No update on draw
    return weights


def play_game(weights):
    game = tic_tac_toe_ai.TicTacToeAi()
    while True:
        current_player = "X" if game.xTurn else "O"
        if (current_player == "X"):
            i, j = tic_tac_toe_ai.calculate_position(choose_move(game.board, weights))
            game.make_move(i, j)
        elif (current_player == "O"):
            i_ai, j_ai = choose_best_move(game.board, "X")
            game.make_move(i_ai, j_ai)
            game.print_board()
        if game.calculate_draw():
            return "draw"
        if game.calculate_winner():
            return "win" if game.calculate_winner() == "X" else "loss"


# Training loop
# AI learner is always X
def train_system(number_of_games):
    learning_rate = 0.5
    results = {"win": 0, "loss": 0, "draw": 0}
    weights = initialize_weights()
    for _ in range(number_of_games):
        outcome = play_game(weights)
        weights = update_weights(weights, outcome, learning_rate)
        results[outcome] += 1
        print(weights)
    
    return results, weights


# Plotting results (use matplotlib or any other plotting library)
def plot_results(results):
    # Implement plotting logic here
    pass
