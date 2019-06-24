'''
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
'''
def reverseStr(s):
    res = s.split(' ')
    return ' '.join(res[::-1])

def reverseStr2(s):
    reverse = s[::-1]
    word = ''
    res = ''
    for i in reverse:
        if i != ' ':
            word += i
        else:
            res += word[::-1]
            res += ' '
            word = ''
    res += word[::-1]
    return res

# print(reverseStr2('jane is a student.'))

# def Reverse(s):
#     start=0
#     end=len(s)-1
#     while(start<end):
#         s[start],s[end]=s[end],s[start]
#         start+=1
#         end-=1
#     return s

'''
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出
'''
def rotateStr(s,n):
    if s=='' or len(s)<=n:
        return s
    return s[n:]+s[:n]


def rotateStr2(s,n):
    if len(s)<=0 or len(s)<n or n<0:
        return None
    front = s[:n][::-1]
    last = s[n:][::-1]
    return reverseStr((front+last)[::-1])


print(rotateStr2('abcde',3))