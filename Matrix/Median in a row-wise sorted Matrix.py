from typing import *

#Naive method

# class Solution:
#     def median(self, matrix, r, c):
#         # code here
#         for i in range(1, r):
#             matrix[0] += matrix[i]
#         for i in range(1, r):
#             matrix.pop()
#
#         matrix[0].sort()
#
#         l = len(matrix[0])
#
#         if l % 2 == 0:
#             a1 = l - 1 // 2
#             a2 = a1 + 1
#             median = (matrix[0][a1] + matrix[0][a2] / 2)
#             return median
#         else:
#             median = matrix[0][l // 2]
#             return median
