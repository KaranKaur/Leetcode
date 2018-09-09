""""

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never
differ by more than 1

"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def height_balanced(root):
    nodes = [root]
    for node in nodes:
        nodes += nodes.left, nodes.right

    depth = {None:0}
    for node in reversed(nodes):
        if node:
            left, right = depth[node.left], depth[node.right]
            if abs(left-right) > 1:
                return False
            depth[node] = 1 + max(left, right)
    return True