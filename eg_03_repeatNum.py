"""
数组长度n， 所有书在0~n-1。找出重复的数
"""

# 法1 排序一个长度为n的数组，需要O(nlogn)时间
# 法2 哈希表 时间，空间O(n)
# 法3 数字m下标是否是i，是则扫描下一个数字，
#     否则和第m个数字比较，若相等，则找到，若不等，交换位置

def repeatNum(nums):
    for i in (nums):
        while i != nums[i]:
            num = nums[i]
            if nums[i] == nums[num]:
                return num
            else:
                t = nums[i]
                nums[i] = nums[num]
                nums[num] = t
    return None


print(repeatNum([4,2,3,3,1,0]))


"""
数组长度n+1, 所有数在1~n，找出重复的数。不修改数组
"""

# 方法： 把数字从中间的数字m分为两半，1~m,m+1~n，
#       如果前一半数字数目超过m，该半中包含重复的数字， 以此类推

def repeatNum1(nums):
    start = 1
    end = len(nums)
    while end >= start:
        mid = start + (end-start)//2
        count = countNum(nums,start,mid)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > mid-start+1:
            end = mid
        else:
            start = mid + 1
    return None
    

def countNum(nums,start,end):
    count = 0
    for i in range(len(nums)):
        if nums[i] >= start and nums[i] <= end:
            count +=1
    return count


print(repeatNum1([4,2,3,3,1,5]))