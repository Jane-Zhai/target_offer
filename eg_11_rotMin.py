'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

def rotMin(nums):
    if nums is None:
        return 0
    first = 0
    last = len(nums)-1
    
    while nums[first] >= nums[last]:
        if last - first == 1:
            mid = last
            break
        mid = first + (last-first)//2
        if nums[mid]==nums[last] and nums[first]==nums[mid]:
            for i in range(first,last):
                if nums[i]>nums[i+1]:
                    return nums[i+1]
        if nums[mid]>=nums[first]:
            first = mid
        elif nums[mid]<=nums[last]:
            last = mid
    return nums[mid]


print(rotMin([1,1,1,0,1]))