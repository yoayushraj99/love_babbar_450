# Difficulty - Medium
from typing import *


class Solution:
    def printSubsequence(self, s, output, index):
        if index >= len(s):
            print(output, end=" ")
            return
        # pick
        self.printSubsequence(s, output+s[index], index+1)
        # Don't pick
        self.printSubsequence(s, output, index+1)


output = ""
input = "abc"

Solution().printSubsequence(input, output, 0)
