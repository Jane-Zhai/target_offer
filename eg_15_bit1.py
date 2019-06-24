'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
# 注意到每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，那么二进制数中的1的个数就会减少一个，
# 因此可以利用一个循环，使得 n = n&(n-1) ，计算经过几次运算减少到0，就是有几个1

def bitone(num):
    count = 0
    if num<0:
        num = num & 0xffffffff  # 复数用补码表示
    while num:
        num = num & (num-1)
        count += 1
    return count


print(bitone(-5))

# 判断一个数是不是2得整数次幂，
# 如果是的话，这个数的二进制数中有且只有一个1，那么这个数n会有 n&(n-1) == 0
def powerOf2(n):
    if n&(n-1) == 0:
        return True
    else:
        return False

# 判断两个数的二进制表示有多少位不一样, 比较两个数的二进制异或，统计异或结果1的个数
def andOr(m, n):
    diff = m^n
    count = 0
    while diff:
        count += 1
        diff = diff&(diff-1)
    return count