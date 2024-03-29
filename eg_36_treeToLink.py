'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

def treeToLink(root):
    if root is None:
        return None
    if not root.left and not root.right:
        return root

    treeToLink(root.left)
    left = root.left

    if left:
        while left.right:
            left = left.right
        root.left, left.right = left, root

    treeToLink(root.right)
    right = root.right

    if right:
        while right.left:
            right = right.left
        root.right, right.left = right, root

    while root.left:
        root = root.left

    return root


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


newList = treeToLink(pNode1)
print(newList.val)