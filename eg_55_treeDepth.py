'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeDepth(node):
    if node is None:
        return 0
    return max(treeDepth(node.left),treeDepth(node.right))+1


'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。(左右子树深度小于1)
'''
def isBalaced(root):
    if root is None:
        return True
    left = treeDepth(root.left)
    right = treeDepth(root.right)
    diff = abs(left-right)
    if diff>1:
        return False
    return isBalaced(root.left) and isBalaced(root.right)


# 遍历一遍
class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        left = 1 + self.getDepth(pRoot.left)
        right = 1 + self.getDepth(pRoot.right)

        if abs(left - right) > 1:
            self.flag = False

        return left if left > right else right



pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
# pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
# pNode3.left = pNode6
# pNode3.right = pNode7

print(treeDepth(pNode1))
S = Solution()
print(S.IsBalanced_Solution(pNode1))