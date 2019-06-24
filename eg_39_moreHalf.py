'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
def MoreHalf(nums):
    if nums==[]:
        return None
    # 若存在则该数出现次数比其他所有数字出现次数之和还要多，则要找的数字肯定是最后一次把次数设为1时对应的数字
    res = nums[0]
    i = 1
    for num in nums[1:]:
        if num == res:
            i += 1
        else:
            i -= 1
        if i == 0:
            res = num
            i = 1
    # 检查其次数是否大于数组的一半
    times = 0
    for num in nums:
        if num == res:
            times += 1
    if times*2 <= len(nums):
        return None
    return res

print(MoreHalf([1])) 