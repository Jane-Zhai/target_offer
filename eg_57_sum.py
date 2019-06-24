'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''

# 因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小
# 所以直接输出查找到的第一对数即可
def findNumsSum(nums,k):
    start = 0
    end = len(nums)-1
    while start<end and nums[start]+nums[end]!=k:
        if nums[start]+nums[end]>k:
            end -= 1
        else:
            start += 1
        if start>=end:
            return None
    return [nums[start],nums[end]]


# print(findNumsSum([1,2,4,7,11,15],15))

'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
# def findContinuousSeq(k):
#     if k<3:
#         return None
#     small = 1
#     big = 2
#     mid = (1+k)//2
#     res = []
#     cursum = small+big

#     while small<mid:
#         if cursum == k:
#             res.append([i for i in range(small,big+1)])
#             small += 1
#         elif cursum < k:
#             big += 1
#         else:
#             small += 1
#         cursum = sum([i for i in range(small,big+1)])
#     return res

def FindContinuousSequence(tsum):
    # write code 
    if tsum<3:
        return []
    small,big=1,2
    middle=(tsum+1)//2
    curSum=small+big
    res=[]

    while (small<middle):
        if curSum==tsum:
            res.append(list(range(small,big+1)))
        while(curSum>tsum and small<middle):
            curSum -= small
            small +=1
            if curSum==tsum:
                res.append(list(range(small,big+1)))
        big+=1
        curSum +=big
    return res

print(FindContinuousSequence(9))