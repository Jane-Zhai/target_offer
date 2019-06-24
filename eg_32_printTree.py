'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

"""
分行从上到下打印二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return None
    queue = [root]
    nextlayer = 0  # 下一层节点数
    tobePrint = 1  # 当前层还没打印节点数
    while queue:
        cur = queue.pop(0)
        tobePrint -= 1
                   
        if cur.left:
            queue.append(cur.left)
            nextlayer += 1
        if cur.right:
            queue.append(cur.right)
            nextlayer += 1

        print(cur.val,end=' ')
        if tobePrint == 0:  # 换行
            print('')
            tobePrint = nextlayer
            nextlayer = 0

'''
之字形打印
'''
def printTree2(root):
    if root is None:
        return None
    queue = [root]
    rqueue = []
    r = 0
    nextlayer = 0  # 下一层节点数
    tobePrint = 1  # 当前层还没打印节点数
    while queue or rqueue:
        if r == 0:
            cur = queue.pop()
            tobePrint -= 1

            
            if cur.left:
                rqueue.append(cur.left)
                nextlayer += 1
            if cur.right:
                rqueue.append(cur.right)
                nextlayer += 1

        else:
            cur = rqueue.pop()
            tobePrint -= 1
            if cur.right:
                queue.append(cur.right)
                nextlayer += 1
            if cur.left:
                queue.append(cur.left)
                nextlayer += 1
            

        print(cur.val,end=' ')
        if tobePrint == 0:  # 换行
            print('')
            tobePrint = nextlayer
            nextlayer = 0
            r ^= 0x1

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(1)
pNode8 = TreeNode(2)
pNode9 = TreeNode(3)
pNode10 = TreeNode(4)
pNode11 = TreeNode(5)
pNode12 = TreeNode(6)
pNode13 = TreeNode(7)
pNode14 = TreeNode(8)
pNode15 = TreeNode(9)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
pNode4.left = pNode8
pNode4.right = pNode9
pNode5.left = pNode10
pNode5.right = pNode11
pNode6.left = pNode12
pNode6.right = pNode13
pNode7.left = pNode14
pNode7.right = pNode15
printTree(pNode1)