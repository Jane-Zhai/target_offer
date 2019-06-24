"""01234567891011...序列化，找任意n为对应的数字"""
def digitAtIndex(index):
    if index < 0:
        return -1
    digit = 1
    while True:
        numbers = countNum(digit)
        if index < numbers * digit:
            return findDigit(index, digit)
        index -= digit * numbers
        digit += 1


# digit位的数字有几个
def countNum(digit):
    if digit == 1:
        return 10
    count = 10 ** (digit-1)
    return 9 * count


# 要找的数字是啥
def findDigit(index, digit):
    if digit == 1:
        begin = 0
    else:
        begin = 10 ** (digit-1)

    number = begin + index//digit
    indexFromRight = digit - index%digit
    for i in range(1,indexFromRight):
        number//=10
    return number % 10


print(digitAtIndex(1001))