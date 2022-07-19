# Given a binary tree, find if it is height balanced or not. A tree is height balanced if difference between heights
# of left and right subtrees is not more than one for all nodes of tree.
#
# A height balanced tree
#         1
#      /     \
#    10      39
#   /
# 5
#
# An unbalanced tree
#         1
#      /
#    10
#   /
# 5
#
# Example 1:
#
# Input:
#       1
#     /
#    2
#     \
#      3
# Output: 0
# Explanation: The max difference in height
# of left subtree and right subtree is 2,
# which is greater than 1. Hence unbalanced
#
# Input: Null
# Output: 1

# Method - 1
def height(node):
    return 1 + max(height(node.left), height(node.right)) if node else 0


def isBalanced(root):
    if not root:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False
    return True and isBalanced(root.left) and isBalanced(root.right)


# Method - 2(Optimized)
def dfs(node):
    if not node:
        return 0
    lh = dfs(node.left)
    if lh == -1: return -1
    rh = dfs(node.right)
    if rh == -1: return -1

    if abs(lh - rh) > 1: return -1
    return 1 + max(lh, rh)


def isBalancedOptimised(root):
    return dfs(root) != -1
