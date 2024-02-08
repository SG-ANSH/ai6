def is_safe(board, row, col, n):
    # check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check upper right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if n_queens(board, row+1, n):
                return True
            board[row][col] = 0

    return False

def main():
    n = 4
    board = [[0] * n for _ in range(n)]
    if n_queens(board, 0, n):
        for row in board:
            print(row)
    else:
        print("Solution does not exist")

main()