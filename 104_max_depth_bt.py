class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def max_depth_bt(root):
    return 1 + max(map(max_depth_bt,(root.left, root.right))) if root else 0

