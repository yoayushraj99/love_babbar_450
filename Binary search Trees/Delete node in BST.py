# Difficulty - Medium
from typing import *

class Solution:
    def findMin(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root, key: int):
        if not root:
            return root

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left and not root.right:
                root = None

            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root



