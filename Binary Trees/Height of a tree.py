from typing import *


def height(node) -> int:
    if node is None:
        return 0
    left_node = height(node.left)
    right_node = height(node.right)

    return 1 + max(left_node, right_node)

