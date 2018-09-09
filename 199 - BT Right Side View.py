"""

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom

Example :
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def bt_right_view(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if root:
        level = [root]
        while level:
            res.append(level[-1].val)
            level = [kid for node in level for kid in (node.left, node.right) if kid]
            return res
        