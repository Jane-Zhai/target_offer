'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点）
返回结果为复制后复杂链表的head。
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# 递归法
def clone(root):
    if root is None:
        return None
    newroot = RandomListNode(root.label)
    newroot.random = root.random
    newroot.next = clone(root.next)
    return newroot


# 分解法
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if  pHead==None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)
    
    def CloneNodes(self,pHead):
        '''
        复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
        '''
        pNode=pHead
        while pNode:
            pCloned=RandomListNode(0)
            pCloned.label=pNode.label
            pCloned.next=pNode.next

            pNode.next=pCloned
            pNode=pCloned.next
    
    def ConnectRandomNodes(self,pHead):
        '''
        将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针的后一个结点
        '''
        pNode=pHead
        while pNode:
            pCloned=pNode.next
            if pNode.random!=None:
                pCloned.random=pNode.random.next
            pNode=pCloned.next

    def ReconnectNodes(self,pHead):
        '''
        拆分链表：将原始链表的结点组成新的链表, 复制结点组成复制后的链表
        '''
        pNode=pHead
        pClonedHead=pClonedNode=pNode.next
        pNode.next = pClonedNode.next
        pNode=pNode.next
        while pNode:
            pClonedNode.next=pNode.next
            pClonedNode=pClonedNode.next
            pNode.next=pClonedNode.next
            pNode=pNode.next
        return pClonedHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3
print(clone(node1).random.label)
print(node1.random)
print(clone(node1).random)

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random)
