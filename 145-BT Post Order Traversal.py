"""
145 - Binary Tree Post Order Traversal

"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def post_order(root):
    ans, res, stack = [], [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node)
            stack += (node.left, node.right)
    while res:
        node = res.pop()
        if node:
            ans.append(node.val)
    return ans        