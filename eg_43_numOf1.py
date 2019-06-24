'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''
def numof1(n):
    res = 0
    for i in range(n+1):
        for s in str(i):
            if s == '1':
                res += 1
    return res


def numof12(n):
    res = 0
    for i in range(n+1):
        while i:
            if i%10 == 1:
                res += 1
            i //= 10
    return res
            

print(numof12(13))
