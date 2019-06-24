'''
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字
均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就
不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

三个栈，一个是压栈，一个是出栈，一个是辅助栈，把数据从pushv向stack中压，如果压入数据和popv出栈的栈顶元素一致，
就从pushv和popv中同时弹出去，不要往stack中压了。等到pushv中元素全弹出来之后，判断stack中出栈元素和popv中出栈
元素是否一致，当popv中元素全部弹出，就结束，说明是一致的
'''

def isPopOrder(push,pop):
    stack = []
    while pop:
        # 第一个元素都相同
        if push and push[0]==pop[0]:
            push.pop()
            pop.pop()
        elif stack and stack[-1]==pop[0]:
            stack.pop()
            pop.pop(0)
        elif push:
            stack.append(push.pop(0))
        else:
            return False
    return True
