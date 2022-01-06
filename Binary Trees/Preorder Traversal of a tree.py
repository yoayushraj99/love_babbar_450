from typing import *

class Solution:
    def preOrder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)
