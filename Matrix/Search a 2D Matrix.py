from typing import *


# Brute force Approach (O(n^2))

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for i in matrix:
#             for j in i:
#                 if j==target:
#                     return True
#         return False


# Efficient Algo

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = None
        # Find the row in which target could exist

        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                x = matrix[i]
                break
        if x is None:
            return False

        # Now use binary search for targeted array x.
        i = 0
        j = len(x) - 1

        while i <= j:
            mid = (i + j) // 2
            if target > x[mid]:
                i = mid + 1
            elif target < x[mid]:
                j = mid - 1
            else:
                return True
        return False
