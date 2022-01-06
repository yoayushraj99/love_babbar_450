from typing import *


# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, node):
        if node is None:
            return

        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

x = Solution()
x.inOrder(root)
