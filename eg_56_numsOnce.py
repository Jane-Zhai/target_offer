'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数。
数组中出了两个数字之外，其他数字都出现两次，那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵消掉，
那两个不同的数字异或的值不为0，也就是说这两个数的异或值中至少某一位为1。
我们找到结果数字中最右边为1的那一位i，然后一次遍历数组中的数字，如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。
这样任何两个相同的数字就分到了一组，而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，然后再对两个组依次进行异或操作，最后每一组得到的结果对应的就是两个只出现一次的数字。
'''
def numsOnce(nums):
    if len(nums)<2:
        return None
    res = 0
    for i in nums:
        res ^= i
    
    # 找到最右边的是1的位
    index = 0
    while res&1==0 and index<=32:
        res >>= 1
        index += 1

    # 分组
    res1=res2=0
    for i in nums:
        if isBit(i,index):
            res1 ^= i
        else:
            res2 ^= i

    return [res1,res2]

def isBit(num,index):
    num >>= index
    return num&1


# aList = [2, 4, 3, 6, 3, 2, 5, 5]
# print(numsOnce(aList))


'''
一个整型数组里除了1个数字之外，其他的数字都出现了3次。请写程序找出这个只出现一次的数字。

每一位相加，除以3，时间效率O(N)，空间O(1)  （需要固定长度存储每一位的和）
'''
def findOnce(nums):
    bitSum = [0]*32
    for i in nums:
        bitMask = 1
        for j in range(31,-1,-1):
            bit = i & bitMask
            if bit:
                bitSum[j]+=1
            bitMask <<= 1
    res = 0
    for i in range(32):
        res <<= 1
        res += bitSum[i]%3
    return res

print(findOnce([1,1,2,2,3,1,2]))