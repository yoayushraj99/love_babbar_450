# Difficulty - Medium
from typing import *


class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            k, temp, count = s[0], '', 0
            for l in s:
                if k == l:
                    count += 1
                else:
                    temp += str(count) + let
                    k = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s
