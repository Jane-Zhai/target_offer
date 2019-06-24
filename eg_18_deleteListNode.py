"""在O(1)时间内删除链表节点"""
# 当要删除的结点不是尾结点而且不是仅有一个结点的头结点，可以把该结点i的下一个结点j的内容复制到结点i，同时把i结点的next指向j结点的next，然后再删除结点j。
# 如果要删除的链表为单结点链表且待删除的结点就是头结点，需要把头结点置为None，
# 如果删除的结点为链表的尾结点，那么就需要顺序遍历链表，找到尾节点前面一个结点，然后将其next置空。

class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def deleteNode(root,node):
    if root is None or node is None:
        return None
    if node.next:  # 删除的不是尾节点
        pNext = node.next
        node.val = pNext.val
        node.next = pNext.next
        pNext.val = None
        pNext.next = None
    elif node == root:  # 只有一个节点，删除该节点
        root.val = None
        root.next = None
        node.val = None
        node.next = None
    else:  # 多个节点，删除尾节点
        pNode = root
        while pNode.next != node:
            pNode = pNode.next
        pNode.next = None
        node.val = None
        node.next = None
        
    
# node1 = ListNode(10)
# node2 = ListNode(11)
# node3 = ListNode(13)
# node4 = ListNode(15)
# node1.next = node2
# node2.next = node3
# node3.next = node4

# deleteNode(node1, node3)
# print(node3.val)
# deleteNode(node1, node3)
# print(node3.val)
# print(node2.val)
# deleteNode(node1, node1)
# print(node1.val)
# deleteNode(node1, node1)
# print(node1.val)


"""删除链表中重复的节点"""
def deleteDuplication(root):
    if not root:
        return None
    preNode = ListNode()
    preNode.next = root
    last=preNode

    while root and root.next:
        if root.val == root.next.val:
            val = root.val
            while root and root.val==val:
                root=root.next
            last.next = root
        else:
            last = root
            root=root.next
    return preNode.next


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(13)
node5 = ListNode(14)
node6 = ListNode(14)
node7 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

root = deleteDuplication(node1)
while root:
    print(root.val)
    root = root.next
