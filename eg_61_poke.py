    
'''
随机从扑克牌中抽出了5张牌,判断是不是顺子,
大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''
def isContinuous(nums):
    numJoker = 0
    for i in range(5):
        if nums[i] == 'A':    nums[i] = 1
        if nums[i] == 'J':    nums[i] = 11
        if nums[i] == 'Q':    nums[i] = 12
        if nums[i] == 'K':    nums[i] = 13
        if nums[i] == 'JOKER':
            nums[i] = 0
            numJoker += 1
        
    nums.sort()
    gap = 0
    for i in range(numJoker+1,5):
        if nums[i] == nums[i-1]:  # 出现对子
            return False

        gap += nums[i] - nums[i-1] - 1

    if gap<=numJoker:
        return True
    else:
        return False



print(isContinuous([9,10,'JOKER','J','JOKER']))