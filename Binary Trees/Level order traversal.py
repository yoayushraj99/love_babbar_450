# Also known as BFS(Breadth first search)

from typing import *
from collections import deque

class Solution:
    def leverOrder(self, root) -> List:
        arr = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            arr.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return arr
