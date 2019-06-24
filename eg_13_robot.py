"""
m行n列方格，机器人从（0,0）开始移动，每次可以向左右上下移动一格，
但不能进入行坐标和列坐标数位之和（每位数字相加）大于k的格子，机器人能到达多少个格子
"""

def robot(row,col,k):
    if k<0 or row<=0 or col<=0:
        return 0

    visit = [[0 for i in range(col)] for j in range(row)]
    count = robotCore(row,col,0,0,visit,k)

    return count

def robotCore(row,col,i,j,visit,k):
    count = 0

    if i>=0 and j>=0 and i<row and j<row and (check(i)+check(j)<=k) and not visit[i][j]:
        visit[i][j] = 1
        count = 1 + (robotCore(row,col,i-1,j,visit,k) + 
        robotCore(row,col,i,j-1,visit,k) +
        robotCore(row,col,i+1,j,visit,k) + 
        robotCore(row,col,i,j+1,visit,k))

    return count

def check(num):
    sum_ = 0
    while num>0:
        sum_ += num % 10
        num //= 10
    return sum_

print(robot(11,11,3))