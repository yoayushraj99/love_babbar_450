# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants. The
# tree could also be considered as a subtree of itself.

# Example 1:
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

def isSameTree(s, t):
    if not s and not t:
        return True
    elif not s or not t:
        return False
    else:
        return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)


def isSubTree(root, subRoot):
    if not root:
        return
    return isSameTree(root, subRoot) or isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)
