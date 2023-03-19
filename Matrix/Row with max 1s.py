from typing import *

class Solution:
    def rowWithMax1s(self, arr:List[List[int]], n:int, m:int) -> int:
        # code here
        max_1 = 0
        max_row_index = 0

        curr_1 = 0
        curr_col = m - 1

        for i in range(n):
            while (curr_col >= 0 and arr[i][curr_col] == 1):
                curr_col -= 1
                curr_1 += 1

            if curr_1 > max_1:
                max_1 = curr_1
                max_row_index = i
            curr_1 = 0
            curr_col = m - 1

        if max_1 == 0:
            return -1

        return max_row_index
