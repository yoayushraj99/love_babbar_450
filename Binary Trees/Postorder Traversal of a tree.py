from typing import *

class Solution:
    def postOrder(self, node):
        if node is None:
            return

        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=" ")
