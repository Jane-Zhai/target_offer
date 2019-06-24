"""
长度为N的绳子，剪成m段，最大乘积
"""

# 先不管剪几段
# 动态规划
def cutRope(N):
    if N < 2:
        return 0
    if N == 2:
        return 1
    if N == 3:
        return 2

    products = [0,1,2,3] # 长度为i的绳子剪后最大乘积products[i]
    for i in range(4,N+1):
        products.append(0)
        for j in range(1,i//2+1):
            product = products[j] * products[i-j]
            products[i] = max(products[i],product)
    return products[N]


# 贪婪算法
def cutRope1(N):
    if N < 2:
        return 0
    if N == 2:
        return 1
    if N == 3:
        return 2

    # 尽可能多剪3
    timesOf3 = N//3
    # 剩下4的时候，剪成两段
    if N-timesOf3*3 == 1:
        timesOf3 -= 1
    timesOf2 = (N-timesOf3*3)//2
    return (3**timesOf3) * (2**timesOf2)
    

print(cutRope1(10))