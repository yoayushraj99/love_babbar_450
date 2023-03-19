# Difficulty - Medium
from typing import *

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
        self.next = None


class Solution:
    def setNextNode(self, node, prev=None):
        if not node:
            return prev

        prev = self.setNextNode(node.left, prev)

        if prev:
            prev.next = node

        prev = node

        return self.setNextNode(node.right, prev)

    def printInorderSuccessors(self, node):

        curr = node
        while curr.left:
            curr = curr.left

        while curr.next:
            print(f'{curr.data}->{curr.next.data}', end=" ")
            curr = curr.next
        print()


''' Construct the following tree
              1
            /   \
           /     \
          2       3
         /      /  \
        /      /    \
       4      5      6
             / \
            /   \
           7     8
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

node = Solution()
node.setNextNode(root)
node.printInorderSuccessors(root)
