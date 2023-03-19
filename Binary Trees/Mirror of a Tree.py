from typing import *

# code
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

class Solution:
    def mirrorTree(self, root):
        if root is None:
            return

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)

print("The inorder traversal of the tree before mirroring:", end=' ')
print(inOrder(root))
# 4 2 1 5 3
print()
x = Solution()
x.mirrorTree(root)
print("The inorder traversal of the tree after mirroring:", end=' ')
print(inOrder(root))
