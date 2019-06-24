"""
输入数字n，按顺序打印处从1到最大的n位十进制数
要考虑大数问题：字符串 or 数组
"""

def Print1ToMaxOfNDigits(n):
    if n<=0:
        return None
    number = ['0'] * n
    while not Increment(number):
        printNum(number)

# 在每次增加1后快速判断是不是到达最大的n位数 时间O(1)
def Increment(number):
    isOverflow = False
    nTakeOver = 0
    nLength = len(number)

    for i in range(nLength-1,-1,-1):
        nSum = int(number[i]) + nTakeOver
        if i == nLength-1:
            nSum += 1
        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = str(nSum)
        else:
            number[i] = str(nSum)
            break
    return isOverflow

def printNum(number):
    isBeginning0 = True
    nLength = len(number)
    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            print('%c' % number[i], end='')
    print('')


# Print1ToMaxOfNDigits(2)

# n个从0到9的全排列
def Print1ToMaxOfNDigits2(n):
    if n<=0:
        return None
    
    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecursively(number,n,0)

def Print1ToMaxOfNDigitsRecursively(number,length,index):
    if index == length-1:
        printNum(number)
        return
    for i in range(10):
        number[index+1] = str(i)
        Print1ToMaxOfNDigitsRecursively(number,length,index+1)

Print1ToMaxOfNDigits2(2)