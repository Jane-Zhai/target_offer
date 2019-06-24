"""
题目：表示数值的字符串
题：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

# float转换
def isNum(s):
    try:
        return float(s)
    except:
        return False

print(isNum('1.2e3'))


# 考虑是否有e存在，如果有，e后面必须是整数，如果没有e存在，则判断它是不是普通的数字。
def isNum2(s):
    if not s or len(s)<=0:
        return False
    
    alist = [i.lower() for i in s]
    if 'e' in alist:
        index = alist.index('e')
        front = alist[:index]
        behind = alist[index+1:]
        if '.' in behind or len(behind)==0:
            return False
        return isDigit(front) and isDigit(behind)
    else:
        return isDigit(alist)

def isDigit(alist):
    dotNum=0
    allow_num = ['0', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '+', '-', '.']
    for i in range(len(alist)):
        if alist[i] not in allow_num:
            return False
        if alist[i]=='.':
            dotNum += 1
        if alist[i] in '+-' and i!=0:
            return False
    if dotNum>1:
        return False
    return True
    
print(isNum2('1.2e3'))