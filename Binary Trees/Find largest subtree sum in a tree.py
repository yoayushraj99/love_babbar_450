# Difficulty - Medium
from typing import *

class Solution:
    def findLargestSubtreeSumUtil(self, root, ans):
        # If currentNode if none then return 0.
        if not root:
            return 0
        # Calculate the sum of the subtree at current Node.
        currSum = root.data+self.findLargestSubtreeSumUtil(root.left, ans)+\
                  self.findLargestSubtreeSumUtil(root.right, ans)
        # Update the answer if the current Subtree
        # Sum is greater than answer.
        ans[0] = max(ans[0], currSum)
        # Return current Subtree sum
        # to its parent node
        return currSum

    def findLargestSubtreeSum(self, root):
        # if tree does not exist, then
        # answer is 0.
        if not root:
            return 0

        ans = [float('-inf')]

        self.findLargestSubtreeSumUtil(root, ans)

        return ans[0]

