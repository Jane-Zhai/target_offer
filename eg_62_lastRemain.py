'''
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字

约瑟夫环 递推公式：f[i] = (f[i-1]+m)%i
'''

def LastRemaining_Solution(n, m):
    if n < 1 or m < 1:
        return -1
    remainIndex = 0
    for i in range(2, n+1):
        remainIndex = (remainIndex + m) % i
    return remainIndex

print(LastRemaining_Solution(5,3))