'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可获得的最大利润是多少？
例如，一只股票在某些时间节点的价格为{9,11,8,5,7,12,16,14}。
如果我们能在价格为5的时候买入并在价格为16时卖出，则能获得最大的利润为11.
'''
def profit(nums):
    minprice = nums[0]
    maxprofit = 0
    for i in nums[1:]:
        minprice = min(minprice,i)
        maxprofit = max(maxprofit,i-minprice)
    return maxprofit

print(profit([9,11,8,5,7,12,16,14]))