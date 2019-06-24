'''
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
例如：如果输入数组为[2,3,4,2,6,2,5,1]及滑动窗口大小为3，那么一共存在6个滑动窗口，它们的最大值分别为[4,4,6,6,6,5]
'''

def maxInWin(nums,size):
    if not nums or size<=0:
        return None
    res = []
    if len(nums)>=size and size>=1:
        queue = []  # 存放下标
        for i in range(size):
            while queue and nums[i]>=nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(size,len(nums)):
            res.append(nums[queue[0]])
            while queue and nums[i]>=nums[queue[-1]]:
                queue.pop()
            # 当一个数下标与当前处理数字下标的差，大于等于窗口大小，滑出
            if queue and queue[0]<=i-size:
                queue.pop(0)
            queue.append(i)
        res.append(nums[queue[0]])
    return res


'''
定义一个队列并实现函数max得到队列最大值，
要求max push pop的时间复杂度都是O(1)
'''

