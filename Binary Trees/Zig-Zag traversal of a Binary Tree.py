from typing import *

from collections import deque


class Solution:
    # Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root) -> List:
        # Your code here
        result = []
        dic = {}
        q = deque()
        q.append((root, 0))

        while q:
            node = q.popleft()
            if node[1] not in dic:
                dic[node[1]] = [node[0].data]
            else:
                dic[node[1]].append(node[0].data)

            if node[0].left:
                q.append((node[0].left, node[1] + 1))
            if node[0].right:
                q.append((node[0].right, node[1] + 1))
        for i in sorted(dic):
            if i % 2 != 0:
                result += dic[i][::-1]
            else:
                result += dic[i]
        return result
