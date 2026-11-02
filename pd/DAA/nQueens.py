
def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    # All queens are placed
    if row == n:
        return True

    # Try each column
    for col in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 1

            # Place next queen
            if solve(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main program
n = int(input("Enter the value of N: "))

board = [[0 for j in range(n)] for i in range(n)]

# Place the first Queen
first_col = int(input("Enter column for first Queen (1 to N): "))

if first_col < 1 or first_col > n:
    print("Invalid column!")
else:
    board[0][first_col - 1] = 1

    # Solve remaining rows
    if solve(board, 1, n):

        print("\nFinal N-Queens Matrix:")

        for row in board:
            print(" ".join(map(str, row)))

    else:
        print("\nNo solution exists for the given first Queen position.")
