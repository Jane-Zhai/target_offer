def fibonacci(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = a+b, a
    return a


print(fibonacci(3))

# 青蛙跳台阶，一次可跳上1或2级，求上n级台阶有几种跳法

# 用2*1的小矩形横着或者竖着覆盖一个更大的矩形
# 用8个小矩形，无重叠覆盖一个2*8的大矩形，有几种办法
# 最左边竖着放，剩下f(7)，横着放，下边一定有一个横着放，剩下f(6)
# f(8) = f(7) + f(6)