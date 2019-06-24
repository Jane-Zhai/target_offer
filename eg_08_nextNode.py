"""
给定一棵二叉树和其中一个节点，找出中序遍历的下一个节点
"""
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.father = None
        self.left = None
        self.left = None


def nextNode(root,node):
    if root is None:
        return None
    
    # 有右子树，下一个节点是右子树的最左节点
    if node.right:
        node = node.right
        while node.left:
            res = node.left
        return res
    # 无右子树
    elif node.father:
        # 是父节点的左子节点,下一个节点是父节点
        if node.father.left == node:
            return node.father
        # 是父节点的右子节点
        else:
            while node.father.left != node:
                node = node.father
                if node == root:
                    return root
            return node
    
