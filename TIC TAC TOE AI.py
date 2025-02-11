import math

# Define the board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Function to print the game board
def print_board(board):
    """ Print the game board with continuous grid lines. """
    for i, row in enumerate(board):
        print('      |  '.join(row))
        if i < 2:
            print('-----+-------+------')

# Function to check if there is a winner or a draw
def check_winner(board):
    """ Check if there is a winner or draw. """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check for draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None

# Minimax algorithm to find the best move
def minimax(board, depth, is_maximizing):
    """ Minimax algorithm to find the best move. """
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif winner == 'Draw':
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def best_move(board):
    """ Find the best move for the AI. """
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to play Tic-Tac-Toe with the AI
def play_game():
    """ Play Tic-Tac-Toe with the AI. """
    current_player = 'X'  # Human starts first
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f'{winner} wins!')
            break

        if current_player == 'X':
            # Human move
            while True:
                try:
                    move = input("Enter your move (row and column, separated by space): ")
                    row, col = map(int, move.split())
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        current_player = 'O'
                        break
                    else:
                        print("This cell is already occupied. Try again.")
                except ValueError:
                    print("Invalid input. Please enter row and column numbers separated by a space.")
                except IndexError:
                    print("Invalid input. Please enter row and column numbers between 0 and 2.")
        else:
            # AI move
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                current_player = 'X'

# Start the game
play_game()
