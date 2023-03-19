# Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b)
# over all choices of indexes such that both c > a and d > b.

from typing import *

# def findMaxValue(mat: List[List[int]], N: int) -> int:
#     highest_num = float('-inf')
#     lowest_num = float('inf')
#     l = len(mat)
#
#     c = 0
#     d = 0
#
#     for i in range(l):
#         for j in range(len(mat[i])):
#             if mat[i][j] > highest_num:
#                 highest_num = mat[i][j]
#                 c = i
#                 d = j
#
#     a = 0
#     b = 0
#
#     for i in range(l):
#         for j in range(len(mat[i])):
#             if mat[i][j] < lowest_num and i < c and j < d:
#                 lowest_num = mat[i][j]
#                 a = i
#                 b = j
#
#     max_value = highest_num-lowest_num
#     return max_value
