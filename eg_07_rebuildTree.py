"""
输入某二叉树的前序和中序遍历结果，重建二叉树
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rebuildTree(preorder,midorder):
    if not preorder and not midorder:
        return None
    if set(preorder) != set(midorder):
        return None

    root = TreeNode(preorder[0])
    i = midorder.index(preorder[0])
    root.left = rebuildTree(preorder[1:i+1], midorder[:i])
    root.right = rebuildTree(preorder[i+1:],midorder[i+1:])
    return root


pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
tree = rebuildTree(pre, tin)

