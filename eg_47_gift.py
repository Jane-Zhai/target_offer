"""
在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0），你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿多少价值的礼物？

解题思路：这是一个典型的能用动态规划解决的问题。
定义f(i,j)表示到达坐标(i,j)的格子能拿到的礼物总和的最大值。则f(i,j)=max(f(i-1,j),f(i,j-1))+gift(i,j) 利用循环写代码较为高效。
"""

def maxGift(array, row, col):
    if array==[] or row<=0 or col<=0:
        return 0
        
    # temp = [0 for i in range(col)]
    # for i in range(row):
    #     for j in range(col):
    #         up = 0
    #         left = 0
    #         if i>0:
    #             up = temp[j]
    #         if j>0:
    #             left = temp[j-1]
    #         temp[j] = max(up,left) + array[i*col+j]
    # return temp[-1]

    temp = [0]*col
    up = 0
    for i in range(row):
        for j in range(col):
            left = 0
            if i>0:
                up = temp[j]
            if j>0:
                left = temp[j-1]
            temp[j] = max(up,left) + array[i*col+j]
    return temp[-1]


print(maxGift([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4))



