# Difficulty - Hard

# Given preorder traversal of a binary search tree, construct the BST.
#
# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be the root of the following tree.
#
#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50


from typing import *

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def constBstUtil(self, root, arr):
        if not arr:
            return
        val = arr[0]
        newNode = Node(val)
        if val < root.data:
            root.left = newNode
            self.constBstUtil(root.left, arr[1:])
        else:
            root.right = newNode
            self.constBstUtil(root.right, arr[1:])

    def constBst(self, arr):
        if not arr:
            return
        root = Node(arr[0])
        self.constBstUtil(root, arr[1:])
        return root
