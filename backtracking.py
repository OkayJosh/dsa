def solveNQueens(N):
    def isSafe(board, row, col):
        # Check if the current column is safe
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check the main diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check the anti-diagonal
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, row):
        if row >= N:
            return True

        for col in range(N):
            if isSafe(board, row, col):
                board[row][col] = 1
                if solve(board, row + 1):
                    return True
                board[row][col] = 0  # Backtrack
        return False

    board = [[0] * N for _ in range(N)]
    if solve(board, 0):
        return board
    else:
        return None


class NQueensSolver:
    def __init__(self, N):
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.rows = set()  # Rows where queens are placed
        self.cols = set()  # Columns where queens are placed
        self.main_diagonals = set()  # Main diagonals where queens are placed (r - c)
        self.anti_diagonals = set()  # Anti-diagonals where queens are placed (r + c)

    def place_queen(self, row, col):
        # Place the queen on the board
        self.board[row][col] = 1
        # Mark the row, column, and diagonals as constrained
        self.rows.add(row)
        self.cols.add(col)
        self.main_diagonals.add(row - col)
        self.anti_diagonals.add(row + col)

    def remove_queen(self, row, col):
        # Remove the queen from the board
        self.board[row][col] = 0
        # Remove the constraints for the row, column, and diagonals
        self.rows.remove(row)
        self.cols.remove(col)
        self.main_diagonals.remove(row - col)
        self.anti_diagonals.remove(row + col)

    def is_safe(self, row, col):
        # Check if the cell is not constrained by any other queen
        if row in self.rows or col in self.cols or (row - col) in self.main_diagonals or (
                row + col) in self.anti_diagonals:
            return False
        return True

    def solve_n_queens(self, row=0):
        if row >= self.N:
            return True  # All queens are placed successfully

        for col in range(self.N):
            if self.is_safe(row, col):
                self.place_queen(row, col)
                if self.solve_n_queens(row + 1):
                    return True
                self.remove_queen(row, col)  # Backtrack

        return False  # No valid placement found

    def get_board(self):
        return self.board

    def solve(self):
        if self.solve_n_queens():
            return self.get_board()
        else:
            return None


# Example usage:
solver = NQueensSolver(4)
solution = solver.solve()
for row in solution:
    print(row)
