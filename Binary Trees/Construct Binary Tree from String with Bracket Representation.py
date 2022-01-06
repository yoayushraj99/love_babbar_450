# Difficulty - Medium

from typing import *

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def strToBinaryTree(self, str):
        arr = []
        x = ['(', ')']
        for i in str:
            if i not in x:
                arr.append(i)

        def arrToBinaryTree(arr, i, n):
            if i < n:
                temp = Node(arr[i])
                root = temp

                # Insert left child
                arrToBinaryTree(arr, 2*i+1, n)

                # Insert Right Child
                arrToBinaryTree(arr, 2*i+2, n)

            return root

        return arrToBinaryTree(arr, 0, len(arr))
