# Difficulty - Medium
from typing import *

class Solution:
    def printPathUtil(self, root, sum, currSum, path):
        # Empty Node
        if not root:
            return
        currSum += root.data
        # Add current node to the path
        path.append(root.data)

        # Print the required Path
        if currSum == sum:
            print("Path Found", end=" ")
            for i in path:
                print(i, end=" ")
            print()

        # If left node exists
        if root.left:
            self.printPathUtil(root.left, sum, currSum, path)
        # If right node exists
        if root.right:
            self.printPathUtil(root.right, sum, currSum, path)

        # Remove the current element
        # From the path
        path.pop()

    def  printPath(self, root, sum):
        path = []
        self.printPathUtil(root, sum, 0, path)

