'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''
def firstNoRepeat(string):
    dic = dict()
    for s in string:
        dic[s] = dic.get(s,0) + 1
    for s in string:
        if dic[s] == 1:
            return s
    return None

print(firstNoRepeat('abcdad'))
