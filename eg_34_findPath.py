'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

def findPath(root,k):
    if root is None:
        return []
    
    if root.left is None and root.right is None:      
        if root.val == k:
            return [[root.val]]
        else:
            return []
    a = findPath(root.left, k-root.val) + findPath(root.right,k-root.val)
    return [[root.val]+i for i in a ]


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
print(findPath(pNode1,22))