class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def isSubTree(root1,root2):
    res = False
    if root1 and root2:
        if root1.val == root2.val:
            res = subTree(root1,root2)
        if not res:
            res = isSubTree(root1.left, root2)
        if not res:
            res = isSubTree(root1.right,root2)
    return res

def subTree(root1,root2):
    if root2 is None:
        return True
    if root1 is None:
        return False
    if root1.val != root2.val:
        return False
    return subTree(root1.left,root2.left) and subTree(root1.right,root2.right)

    



        