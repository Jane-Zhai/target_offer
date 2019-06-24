'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

# 三步走策略：1 只做各位相加不进位（可以用异或来处理，和异或结果相同）
# 2 进位：可以想象为两个数先做位与运算，然后左移一位
# 3 把前两个步骤的结果相加，重复前两步，直到不产生进位为止。
# 在Python中做位运算，需要做越界检查。
def add(num1,num2):
    while num2:
        add = (num1 ^ num2) & 0xffffffff
        carry = ((num1 & num2) << 1) & 0xffffffff
        num1 = add
        num2 = carry
    if num1 < 0x7fffffff:
        return num1
    else:
        return ~(num1^0xffffffff)

print(add(-3,5))

# 拓展：不使用新的变量，交换两个变量的值。

# 基于加减法           基于异或
# a=a+b                a=a^b
# b=a-b                b=a^b
# a=a-b                a=a^b