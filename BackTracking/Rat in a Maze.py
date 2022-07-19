# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1,
# N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which
# the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that
# it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel
# through it. Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot
# move to any other cell.

# Example 1:
#
# Input:
# N = 4
# m[][] = {{1, 0, 0, 0},
#          {1, 1, 0, 1},
#          {1, 1, 0, 0},
#          {0, 1, 1, 1}}
# Output:
# DDRDRR DRDDRR
# Explanation:
# The rat can reach the destination at
# (3, 3) from (0, 0) by two paths - DRDDRR
# and DDRDRR, when printed in sorted order
# we get DDRDRR DRDDRR.

from typing import *


def isSafe(newx, newy, visited, n, arr):
    if ((0 <= newx < n) and (0 <= newy < n) and
            (visited[newx][newy] == 0) and (arr[newx][newy] == 1)):
        return True
    return False


def utilSearchMaze(x, y, arr, n, vis, out, res):
    # Base Case
    if x == n - 1 and y == n - 1:
        res.append(out)
        return

    # 4 Movements D, L, R, U

    vis[x][y] = 1
    # Down
    newx = x + 1
    newy = y
    if isSafe(newx, newy, vis, n, arr):
        out += "D"
        utilSearchMaze(newx, newy, arr, n, vis, out, res)
        out = out[:-1]

    # Left
    newx = x
    newy = y - 1
    if isSafe(newx, newy, vis, n, arr):
        out += "L"
        utilSearchMaze(newx, newy, arr, n, vis, out, res)
        out = out[:-1]

    # Right
    newx = x
    newy = y + 1
    if isSafe(newx, newy, vis, n, arr):
        out += "R"
        utilSearchMaze(newx, newy, arr, n, vis, out, res)
        out = out[:-1]
    # Up
    newx = x - 1
    newy = y
    if isSafe(newx, newy, vis, n, arr):
        out += "U"
        utilSearchMaze(newx, newy, arr, n, vis, out, res)
        out = out[:-1]
    vis[x][y] = 0


def searchMaze(arr: List[List[int]], n: int):
    # Edge Case
    if arr[0][0] == 0:
        return ""
    # Create a visited array to track the path which we have already visited.
    vis = [[0 for i in range(n)] for j in range(n)]
    res = []
    utilSearchMaze(0, 0, arr, n, vis, "", res)
    return res
