# Tic-Tac Toe

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the player has won the game."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Check if the board is fully occupied."""
    for row in board:
        if " " in row:
            return False
    return True

def play_tic_tac_toe():
    """Play Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)

        player_symbol = players[current_player]
        print(f"Player {player_symbol}'s turn")

        # Get player move
        while True:
            try:
                block = int(input("Enter block number (1-9): "))
                if 1 <= block <= 9:
                    row = (block - 1) // 3
                    col = (block - 1) % 3
                    if board[row][col] == " ":
                        break
                    else:
                        print("Block is already occupied. Try again.")
                else:
                    print("Invalid block number. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Make the move
        board[row][col] = player_symbol

        # Check for win
        if check_winner(board, player_symbol):
            print_board(board)
            print(f"Player {player_symbol} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()
