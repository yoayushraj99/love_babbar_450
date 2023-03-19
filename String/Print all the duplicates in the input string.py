# Difficulty - Easy
from typing import *

class Solution:
    def print_dups(self, s):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        for i, j in dic.items():
            if j > 1:
                print((i, j), end=" ")


dup = Solution()

dup.print_dups("abcbsbdeaaa")
