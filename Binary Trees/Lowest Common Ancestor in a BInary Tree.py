# Difficulty - Medium
from typing import *

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def storePath(self, node, n, path):
        if not root:
            return

        path.append(node.data)
        if node.data == n:
            return

        if node.left:
            self.storePath(node.left, n, path)
        if node.right:
            self.storePath(node.right, n, path)

        path.pop()

    def lca(self, root, n1, n2):
        if not root:
            return
        # Store the path to reach n1
        path1 = []
        self.storePath(root, n1, path1)
        # store the path to reach n2
        path2 = []
        self.storePath(root, n2, path2)

        if path1 and path2:
            # Find the common element in b/w path1 and path2
            for i in range(min(len(path1), len(path2))):
                if path1[i] == path2[i]:
                    return Node(path1[i])

        return Node(-1)
