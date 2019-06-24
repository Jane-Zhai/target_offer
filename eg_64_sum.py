'''
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

# 终止递归采用逻辑与的短路特性
def sum1(n):
    return n and n+sum1(n-1)

# 利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况，
# 如果对n连续进行两次反运算，那么非零的n转换为True，0转换为False。利用这一特性终止递归。
def sum2(n):
    return sumN(n)
def sum0(n):
    return 0
def sumN(n):
    func = {False:sum0, True:sumN}
    f = func[not not n](n-1) 
    return n+func[not not n](n-1) 


print(sum2(4))