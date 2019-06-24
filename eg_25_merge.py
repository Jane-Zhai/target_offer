"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def merge(root1,root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1


    head = cur = ListNode(0)
    while root1 and root2:
        if root1.val < root2.val:
            cur.next = root1
            root1 = root1.next
        else:
            cur.next = root2
            root2 = root2.next
        cur = cur.next
    cur.next = root1 or root2
    return head.next
    

# 递归
def merge2(root1,root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    head = None
    if root1.val < root2.val:
        head = root1
        head.next = merge2(root1.next,root2)
    else:
        head = root2
        head.next = merge2(root1,root2.next)
    return head
        


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

res = merge2(node1,node4)
while res:
    print(res.val)
    res = res.next