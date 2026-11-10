N = int(input())

board = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(1)
    board.append(row)

def place_queen(b, row, col):
    for i in range(N):
        for j in range(N):
            if i == row or j == col or i - j == row - col or i + j == col + row:
                b[i][j] = 0

def copy_board(b):
    return [row[:] for row in b]

def solve(b, row, queens):
    if row == N:
        return queens[:]
    for col in range(N):
        if b[row][col] == 1:
            nb = copy_board(b)
            place_queen(nb, row, col)
            queens.append((row, col))
            result = solve(nb, row + 1, queens)
            if result is not None:
                return result
            queens.pop()
    return None

solution = solve(board, 0, [])

if solution is None:
    print("No solution")
else:
    final = [["." for _ in range(N)] for _ in range(N)]
    for r, c in solution:
        final[r][c] = "Q"
    for row in final:
        print("  ".join(row))