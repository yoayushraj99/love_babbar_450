# Difficulty - Medium
from typing import *

class Solution:
    def sumOfLongRootToLeafPathUtil(self, root, Sum, Len, maxSum, maxLen):
        if not root:
            if maxLen[0]<Len:
                maxSum[0] = Sum
                maxLen[0] = Len
            elif maxLen[0] == Len and maxSum[0] < Sum:
                maxSum[0] = Sum
            return

        self.sumOfLongRootToLeafPathUtil(root.left, Sum+root.data, Len+1, maxSum, maxLen)
        self.sumOfLongRootToLeafPathUtil(root.right, Sum+root.data, Len+1, maxSum, maxLen)

    def sumOfLongRootToLeafPath(self,root):
        if not root:
            return 0
        maxSum = [float('-inf')]
        maxLen = [0]

        self.sumOfLongRootToLeafPathUtil(root, 0, 0, maxSum, maxLen)

        return maxSum[0]
