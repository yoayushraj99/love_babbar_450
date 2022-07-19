# Given the roots of two binary trees
# p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
# Example
# 1:
#
# Input: p = [1, 2, 3], q = [1, 2, 3]
# Output: true
# Example
# 2:
#
# Input: p = [1, 2], q = [1, null, 2]
# Output: false

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
