from typing import *
from collections import deque


class newNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        if not root:
            return
        result = []
        dic = {}
        q = deque()
        q.append((root, 0))

        while q:
            curr = q.popleft()

            if curr[1] not in dic:
                dic[curr[1]] = curr[0].data

            if curr[0].left:
                q.append((curr[0].left, curr[1] - 1))

            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))

        for i in sorted(dic):
            result.append(dic[i])
        return result


""" Create following Binary Tree
        1
       / \
      2   3
       \
        4
         \
          5
           \
            6
"""

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
print("Following are nodes in top view of Binary Tree")
x = Solution()
print(x.topView(root))
