"""
输入一个链表头节点，从尾到头打印每个节点的值
"""
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def printList(node):
    if node is None:
        return None
        
    stack = []
    while node:
        stack.append(node)
        node = node.next
    while stack:
        node = stack.pop()
        print(node.val, end=' ')

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
printList(None)