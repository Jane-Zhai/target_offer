'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
def PrintMinNumber(numbers):
    # write code here
    if len(numbers)<=0:
        return ""
    str_numbers=[str(i) for i in numbers]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if str_numbers[i]+str_numbers[j] > str_numbers[j]+str_numbers[i]:
                str_numbers[i],str_numbers[j] = str_numbers[j],str_numbers[i]
    return ''.join(str_numbers)


numbers = [3, 32, 321]
print(PrintMinNumber(numbers))
