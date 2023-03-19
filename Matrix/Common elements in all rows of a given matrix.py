# Use Dictionary

from typing import *


class Solution:
    def printCommonElements(self, mat: List[List[int]], M: int, N: int):
        mp = dict()

        for j in range(N):
            mp[mat[0][j]] = 1

        for i in range(1, M):
            for j in range(N):
                # Check if the element is present in mp
                # if it present then increase by 1
                # Also check the element is not duplicated in current row
                if (mat[i][j] in mp and mp[mat[i][j]] == i):
                    mp[mat[i][j]] = i+1

                    if i == M-1:
                        print(mat[i][j], end=" ")


mat = [[1, 2, 0, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

matrix = Solution()

matrix.printCommonElements(mat, 4, 5)
