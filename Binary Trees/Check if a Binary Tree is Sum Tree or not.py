# Difficulty - Medium
from typing import *


class Solution:
    def sum(self, root):
        if not root:
            return 0
        old = root.data
        root.data = self.sum(root.left) + self.sum(root.right)
        return root.data + old

    def isSumTree(self, root):
        # Code here
        if root:
            leftSum = self.sum(root.left)
            rightSum = self.sum(root.right)
            if leftSum != 0 and rightSum != 0:
                if root.data != leftSum + rightSum:
                    return False
            self.isSumTree(root.left)
            self.isSumTree(root.right)
            return True
