from typing import *


class Solution:

    def __init__(self):
        self.result = []

    def printBoundaryLeft(self, root):
        if root:
            if root.left:
                self.result.append(root.data)
                self.printBoundaryLeft(root.left)
            elif root.right:
                self.result.append(root.data)
                self.printBoundaryLeft(root.right)

    def printLeaf(self, root):
        if root:
            self.printLeaf(root.left)

            if root.left is None and root.right is None:
                self.result.append(root.data)
            self.printLeaf(root.right)

    def printBoundaryRight(self, root):
        if root:
            if root.right:
                self.printBoundaryLeft(root.right)
                self.result.append(root.data)
        elif root.left:
            self.printBoundaryLeft(root.left)
            self.result.append(root.data)


def printBoundaryView(self, root):
    self.result.append(root.data)
    self.printBoundaryLeft(root.left)
    self.printLeaf(root.left)
    self.printLeaf(root.right)
    self.printBoundaryRight(root.right)
    return self.result
