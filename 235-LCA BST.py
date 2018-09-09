"""
Given a BST, find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants
(where we allow a node to be a descendant of itself).

Example: Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

1)Given : root, p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

2) Given : root, p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.

"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def lca_bst(root, p, q):
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root

