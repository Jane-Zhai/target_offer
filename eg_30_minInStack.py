'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
在该栈中，调用min、push、pop的时间复杂度都是O(1)

思路：把每次的最小元素保存起来放在另一个辅助栈里。
'''
class stack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def pop(self):
        if self.stack == []:
            return None
        self.stack.pop()
        self.minStack.pop()

    def push(self,x):
        self.stack.append(x)
        if self.minStack == [] or x<=self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def min(self):
        return self.minStack[-1]


S = stack()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())
