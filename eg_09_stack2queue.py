"""
用两个栈实现一个队列，在队列尾部插入节点，头部删除节点的功能
"""
# 需要两个栈Stack1和Stack2，push的时候直接push进Stack1。
# pop需要判断Stack1和Stack2中元素的情况，Stack2不为空的话，直接从Stack2 pop，
# stack2为空，但Stack1不空，把Stack1的元素push进入Stack2，然后pop Stack2的值
class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self,k):
        self.stack1.append(k)

    def deleteHead(self):
        if not self.stack1 and not self.stack2:
            return
        elif not self.stack2:
            while self.stack1:
                cur = self.stack1.pop()
                self.stack2.append(cur)
        return self.stack2.pop()


# P = queue()
# P.appendTail(10)
# P.appendTail(11)
# P.appendTail(12)
# print(P.deleteHead())
# P.appendTail(13)
# print(P.deleteHead())
# print(P.deleteHead())
# print(P.deleteHead())
# print(P.deleteHead())


# 两个队列实现栈
class stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def appendTail(self,k):
        if not self.queue1:
            self.queue2.append(k)
        elif not self.queue2:
            self.queue1.append(k)
        

    def deleteTail(self):
        while not self.queue1 and not self.queue2:
            return 
        while not self.queue2:
            for i in range(len(self.queue1)-1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        while not self.queue1:
            for i in range(len(self.queue2)-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

P = stack()
P.appendTail(10)
P.appendTail(11)
P.appendTail(12)
print(P.deleteTail())
P.appendTail(13)
print(P.deleteTail())
print(P.deleteTail())
print(P.deleteTail())
print(P.deleteTail())