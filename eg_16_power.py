"""
乘方
"""

# 如果采用常规解法，需要注意的地方:当指数为负数的时候；当底数为零且指数为负数的情况；
# 在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,
# 只能判断他们的差的绝对值是不是在一个很小的范围内
def power(base,exponent):
    if base == 0 and exponent<0:
        return None

    if exponent<0:
        absExponent = -exponent
    else:
        absExponent = exponent

    result = 1.0
    for i in range(absExponent):
        result *= base

    if exponent<0:
        result = 1.0/result

    return result

# 递归
'''
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
'''
def power2(base,expoent):
    if expoent == 0:
        return 1
    if expoent == 1:
        return base
    if expoent == -1:
        return 1/base

    result = power2(base,expoent>>1)
    result *= result
    if expoent & 0x1 == 1:
        result *= base

    return result


print(power2(2,-8))

