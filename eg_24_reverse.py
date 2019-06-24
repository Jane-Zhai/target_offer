'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def reverse(root):
    if root is None:
        return None
        
    pRev = None
    p = root
    
    while p:
        pRev, pRev.next, p = p, pRev, p.next

    return pRev

        

        
data = [1,2,3,4]
head = ListNode(data[0])
cur = head
for i in data[1:]:
    cur.next = ListNode(i) 
    cur = cur.next

cur = reverse(head)
while cur:
    print(cur.val, end=" ")
    cur = cur.next
print("")       