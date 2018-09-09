"""
Binary Tree In Order Traversal

In Order = left, root, right

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_trav(root):
    ans, stack = [], []
    while stack or root:

        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            ans.append(node.val)
            root = node.right
    return ans
