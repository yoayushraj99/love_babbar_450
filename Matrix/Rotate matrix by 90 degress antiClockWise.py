#Given a square matrix, turn it by 90 degrees in a clockwise direction
# without using any extra space.

from typing import *

def printMatrix(mat: List[List[int]], n: int) -> List[List[int]]:
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()

def rotateMatrix(mat: List[List[int]], n: int):
    # Take transpose of the matrix
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # reverse indivisual row
    for i in range(n):
        low, high = 0, n-1
        while low < high:
            mat[i][low], mat[i][high] = mat[i][high], mat[i][low]
            low += 1
            high -= 1

    printMatrix(mat, n)


rotateMatrix([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]], 4)

