'''
操作给定的二叉树，判断是否为镜像。
'''
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

def isMirror(root):
    return check(root,root)
def check(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return check(root1.left,root2.right) and check(root1.right,root2.left)


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(6)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(7)
pNode7 = TreeNode(5)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

print(isMirror(pNode1))