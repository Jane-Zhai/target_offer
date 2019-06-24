'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# 对每一个数都需要判断它是不是丑数（需要执行求余和除法操作） 
# 大数就跪了
def getUglyNum(N):
    if N <= 0:
        return 0   
    num = 0
    uglyNum = 0
    while uglyNum<N:
        num += 1
        if isUgly(num):
            uglyNum += 1
    return num 

def isUgly(num):
    while num%2==0:
        num//=2
    while num%3==0:
        num//=3
    while num%5==0:
        num//=5
    return True if num==1 else False


# 空间换时间
def getUglyNum2(N):
    if N <= 0:
        return 0
    res=[1]
    nextIndex = 1
    t2 = t3 = t5 = 0
    while nextIndex<N:
        min_val = min(res[t2]*2,res[t3]*3,res[t5]*5)
        res.append(min_val)
        while res[t2]*2 <= min_val:
            t2 += 1
        while res[t3]*3 <= min_val:
            t3 += 1
        while res[t5]*5 <= min_val:
            t5 += 1
        nextIndex += 1
    return res[N-1]



print(getUglyNum2(1500))