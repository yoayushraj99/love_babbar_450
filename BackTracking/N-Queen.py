# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
# other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
# queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
#
# Input: n = 1
# Output: [["Q"]]

from typing import *


def addSum(board, ans, n):
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(board[i][j])

    ans.append(temp)


def isSafe(row, col, board, n):
    # As we move from left to right we don't need to check the right cols of queen(because it is empty).
    # That's why we will only check the left cols of the queen we place.
    x = row
    y = col

    # Check for same row
    while y >= 0:
        if board[x][y] == 1:
            return False
        y -= 1

    # Now we don't need to check the column because we are placing a queen, and then we move on.

    # Check for diagonal
    x = row
    y = col

    # Check for top left Diagonal Elements
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1

    # Check for down left diagonal Elements
    x = row
    y = col
    while x < n and y >= 0:
        if board[x][y] == 1:
            return False
        x += 1
        y -= 1

    return True


def solve(col, ans, board, n):
    # Base
    if col == n:
        addSum(board, ans, n)
        return

    # Solve 1 case and rest recursion will take care
    for row in range(n):
        if isSafe(row, col, board, n):
            # If placing queen is safe
            board[row][col] = 1
            solve(col + 1, ans, board, n)
            board[row][col] = 0


def nQueens(n: int):
    board = [[0 for i in range(n)] for j in range(n)]
    ans = []
    solve(0, ans, board, n)
    return ans


print(nQueens(4))
