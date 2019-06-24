class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None

'''
输入一个链表，输出该链表中倒数第k个结点。(从1开始计数)
'''

'''
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点,然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点

推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''
def findKthtoTail(root,k):
    if not root or k<=0:
        return None

    pHead = root
    pBehind = root

    for i in range(k-1):
        if pHead.next:
            pHead = pHead.next
        else:  # 链表节点数小于k
            return None

    while pHead.next:
        pHead = pHead.next
        pBehind = pBehind.next
    return pBehind


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

print(findKthtoTail(node1, 1).val)