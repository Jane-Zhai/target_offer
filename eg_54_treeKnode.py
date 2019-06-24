"""
给定一颗二叉搜索树，请找出其中的第k小的结点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def KthNode(pRoot, k):
    if not pRoot or k<=0:
        return None
    res=[]
    
    def inorder(pRoot):
        if not pRoot:
            return []
        inorder(pRoot.left)
        res.append(pRoot)
        inorder(pRoot.right)
    inorder(pRoot)
    if len(res)<k:
        return None
    return res[k-1]



pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

print(KthNode(pNode1,3).val)