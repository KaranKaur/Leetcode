"""

Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes
overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def merge_bt(t1, t2):
    if t1 and t2:
        root = TreeNode(t1.val + t2.val)
        root.left = merge_bt(t1.left, t2.left)
        root.right = merge_bt(t1.right, t2.right)
        return root
    else:
        return t1 or t2
