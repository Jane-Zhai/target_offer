class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


def Serialize(root):
    if root is None:
        return '#'
    return str(root.val) + ' ' + Serialize(root.left) + ' ' + Serialize(root.right)


flag = -1
def deSerialize(s):
    global flag
    flag += 1 
    lis = s.split(' ')
    if flag >= len(s):
        return None
    root = None
    if lis[flag] != '#':
        root = TreeNode(int(lis[flag]))
        root.left = deSerialize(s)
        root.right = deSerialize(s)
    return root
        

pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
print(Serialize(pNode1))
tree = deSerialize(Serialize(pNode1))
print(Serialize(tree))
