from typing import *
from collections import deque

class Solution:
    def diagonalTraversal(self, root) -> List:
        result = []
        # Queue to store the left nodes
        left_q = deque()

        node = root

        while node:
            result.append(node.data)

            # if left available add it to the queue
            if node.left:
                left_q.appendleft(node.left)
            # if right is available change the node
            if node.right:
                node = node.right
            else:
                # else pop the left queue
                if len(left_q) >= 1:
                    node = left_q.pop()
                else:
                    node = None

        return result
