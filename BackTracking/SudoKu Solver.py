# You have been given a 9x9 2d integer matrix 'MAT' representing a Sudoku puzzle. The empty cells of the Sudoku are
# filled with zeros, and the rest of the cells are filled with integers from 1 to 9. Your task is to fill all the
# empty cells such that the final matrix represents a Sudoku solution.

# Note: A Sudoku solution must satisfy all the following conditions-
# 1. Each of the digits 1-9 must occur exactly once in each row.
# 2. Each of the digits 1-9 must occur exactly once in each column.
# 3. Each of the digits 1-9 must occur exactly once in each of the 9, 3x3 sub-grids of the grid.
#
# You can also assume that there will be only one sudoku solution for the given matrix.

from typing import *


def isSafe(row, col, board, val, n) -> bool:
    # Row Check
    for i in range(n):
        if board[row][i] == val:
            return False
        # Col Check
        if board[i][col] == val:
            return False
        # 3 x 3 Matrix Check
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == val:
            return False

    return True


def solve(board) -> bool:
    n = len(board[0])

    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                for val in range(1, 10):
                    if isSafe(row, col, board, val, n):
                        board[row][col] = val
                        nextSolPossible = solve(board)
                        if nextSolPossible:
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True


def solveSudoku(sudoku):
    solve(sudoku)


suDoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

solveSudoku(suDoku)
print(suDoku)
