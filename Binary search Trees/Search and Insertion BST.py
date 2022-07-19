# Difficulty - Easy
from typing import *

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def __init__(self, val):
        self.root = Node(val)

    def search(self, root, key):
        if not root:
            print("Hu hi nhi toh milunga kaha se bsdk")
            return False
        if root.data == key:
            print("Mil gya Abb so ja bsdk")
            return
        if key < root.data:
            self.search(root.left, key)
        else:
            self.search(root.right, key)

    def insert(self, key, node):
        if not node:
            return Node(key)

        if key < node.data:
            node.left = self.insert(key, node.left)
        else:
            node.right = self.insert(key, node.right)
        return node

    def printBst(self, root):
        if not root:
            return
        print(root.data, end = " ")
        self.printBst(root.left)
        self.printBst(root.right)

bst = Solution(10)
bst.insert(1, bst.root)
bst.insert(5, bst.root)
bst.insert(3, bst.root)
bst.insert(4, bst.root)
bst.printBst(bst.root)
print()
bst.search(bst.root, 6)
