'''
统计一个数字在排序数组中出现的次数。

二分查找法，分别找到此数字在排序数组中第一次和最后一次出现的位置，然后次数等于两个位置之差加1。
时间复杂度：O(log n)
'''

def getNumK(nums,k):
    if nums == []:
        return None
    length = len(nums)
    first = getFirst(nums,k,0,length-1)
    last = getLast(nums,k,0,length-1)
    if first > -1 and last > -1:
        number = last - first + 1
    else:
        number = 0
    return number

def getFirst(nums,k,start,end):
    if start>end:
        return -1
    mid = start + (end-start)//2
    if nums[mid] == k:
        if mid > 0 and nums[mid-1]==nums[mid]:
            end = mid-1           
        else:
            return mid
    elif nums[mid] > k:
        end = mid-1
    else:
        start = mid+1
    return getFirst(nums,k,start,end)

def getLast(nums,k,start,end):
    if start>end:
        return -1
    mid = start + (end-start)//2
    if nums[mid] == k:
        if mid < end and nums[mid+1]==nums[mid]:
            start = mid+1
        else:
            return mid
    elif nums[mid] > k:
        end = mid-1
    else:
        start = mid+1
    return getLast(nums,k,start,end)
    
# print(getNumK([2,2,2,3,4],4))


"""递增数列，0-n-1中缺失数字"""
def miss(nums):
    start = 0
    end = len(nums)-1
    num = findMiss(nums,start,end)
    return num

def findMiss(nums,start,end):
    while start<=end:
        mid = start + (end-start)//2
        if nums[mid] == mid:
            start = mid+1
        elif mid == 0 or nums[mid-1] == mid-1:
            return mid
        else:
            end = mid-1
        return findMiss(nums,start,end)
    return -1

# print(miss([1,2,3,4]))


"""递增数列，数组中数值和下标相等的元素"""
def same(nums):
    start = 0
    end = len(nums)-1

    num = findSame(nums,start,end)
    return num

def findSame(nums,start,end):
    mid = start + (end-start)//2
    while start<=end:
        if nums[mid] == mid:
            return mid
        if nums[mid] > mid:
            end = mid-1
        else:
            start = mid+1
        return findSame(nums,start,end)
    return -1

print(same([-3,-1,1,3,5]))