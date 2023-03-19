# Difficulty - Easy
from typing import *


class Solution:
    def __init__(self):
        self.leafLevel = 0

    def checkUtil(self, root, level):
        if not root:
            return True

        if root.left is None and root.right is None:
            if self.leafLevel == 0:
                self.leafLevel = level
                return True

            return level == self.leafLevel
        return self.checkUtil(root.left, level + 1) and self.checkUtil(root.right, level + 1)

    def check(self, root):
        # Code here
        return self.checkUtil(root, 0)
