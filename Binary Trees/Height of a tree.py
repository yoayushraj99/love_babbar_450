from typing import *

class Solution:
    def height(self, node) -> int:
        if node is None:
            return 0
        left_node = height(node.left)
        right_node = height(node.right)

        return 1 + max(left_node, right_node)

