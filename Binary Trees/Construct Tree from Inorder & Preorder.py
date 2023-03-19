# Difficulty - Medium

from typing import *


# Node class

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def __init__(self):
        self.preindex = 0
        self.dic = {}

    def build(self, preorder, start, end):
        if start > end:
            return None

        curr = preorder[self.preindex]
        self.preindex += 1
        tNode = Node(curr)

        if start == end:
            return tNode

        inIndex = self.dic[curr]

        tNode.left = self.build(preorder, start, inIndex - 1)
        tNode.right = self.build(preorder, inIndex + 1, end)
        return tNode

    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        for i in range(n):
            self.dic[inorder[i]] = i

        root = self.build(preorder, 0, n - 1)
        return root
