'''
输入两个链表，找出它们的第一个公共结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def commonNode(node1,node2):
    length1 = lenNode(node1)
    lenght2 = lenNode(node2)
    if lenght2>length1:
        n = lenght2-length1
        longhead = lenght2
        shorthead = length1
    else:
        n = length1-lenght2
        longhead = length1
        shorthead = lenght2

    node = longhead
    while n:
        node = node.next
        n -= 1
    lcurnode = node
        
    scurnode = shorthead
    while scurnode:
        if lcurnode == scurnode:
            return lcurnode
        lcurnode = lcurnode.next
        scurnode = scurnode.next

def lenNode(node):
    l = 0
    while node:
        node = node.next
        l += 1
    return l


