# Difficulty - Easy
from typing import *


class Solution:
    def maxSubStr(self, s):
        cnt_0 = 0
        cnt_1 = 0

        cnt = 0

        for value in s:
            if value == "0":
                cnt_0 += 1
            else:
                cnt_1 += 1

            if cnt_0 == cnt_1:
                cnt += 1

        if cnt_0 != cnt_1:
            return -1
        return cnt


x = Solution()
print(x.maxSubStr("011110001010"))
