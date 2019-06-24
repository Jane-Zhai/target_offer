"""
题目：如果一个链表中包含环，如何找出环的入口节点？

解题分析：其实此题可以分解为三个题目：1）如何判断一个链表中是否包含环？2）如何找到环的入口节点？3）如何得到环中节点的数目？

解决此题：可以设置两个指针，一快一慢。
1.两个指针一个fast、一个slow同时从一个链表的头部出发
  fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇，（如果相遇就证明此链表包含环，否则没有环，解决问题1）
2.1 此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
    这次两个指针一次走一步，相遇的地方就是入口节点（解决问题2，得到环的入口节点）。
2.2  接着步骤1，如果两个指针相遇，必然在环内，所以可以从这个节点出发，继续向前移动，并且计数，当再次回到这个节点时，就可以得到环中节点数了（解决问题3，得到环中节点数目）

找到头节点：先确定有环有N个节点，指针1先在链表上移动N步，然后两个指针相同速度前进，相遇处
"""

class ListNode:  
    def __init__(self, x):  
        self.val = x  
        self.next = None  

def circle(root):
    if root is None:
        return None
    pFast = root
    pSlow = root
    while pFast and pFast.next:
        pFast = pFast.next.next
        pSlow = pSlow.next
        if pFast == pSlow:  # 相遇，有环
            pFast = root
            while pFast != pSlow:  
                pFast = pFast.next
                pSlow = pSlow.next
            return pFast  # 再次相遇，环入口
    return None 
    

def circleNum(root):
    if root is None:
        return None
    pFast = root
    pSlow = root
    while pFast and pFast.next:
        pFast = pFast.next.next
        pSlow = pSlow.next
        if pFast == pSlow:  # 相遇，有环
            pSlow = pSlow.next
            count = 1
            while pFast != pSlow:  
                pSlow = pSlow.next
                count += 1
            return count  # 再次相遇，环入口
    return None 


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node4 = ListNode(13)
node5 = ListNode(14)
node6 = ListNode(15)
node7 = ListNode(16)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
# node7.next = node2

print(circle(node1))
print(circleNum(node1))