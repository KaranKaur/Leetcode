"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_trav(root):
    #visit root, left then right. Use stack

    res, nodes = [], [root]
    while nodes:
        node = nodes.pop()
        if node:
            res.append(node.val)
            nodes += (nodes.right, nodes.left)
            #nodes.extend(nodes.right, nodes.left)
    return res
