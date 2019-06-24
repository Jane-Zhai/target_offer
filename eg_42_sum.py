'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''
def sumInNums(nums):
    if nums == []:
        return None

    curSum = 0
    maxSum = nums[0]
    for num in nums:
        if curSum <= 0:
            curSum = num
        else:
            curSum += num
        if curSum > maxSum:
            maxSum = curSum

    return maxSum


def sumInNums2(nums):
    if nums == []:
        return None
    lis = [nums[0]]
    for num in nums[1:]:
        if lis[-1]<=0:
            lis.append(num)
        else:
            lis.append(num+lis[-1])
    return max(lis)

print(sumInNums2([1, -2, 3, 10, -4, 7, 2, -5]))