"""
题目：正则表达式匹配
题：请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
"""
def match(s,pattern):
    if len(s)==0 and not pattern:
        return True
    if len(s)>0 and not pattern:
        return False

    # 模第二个字符是*
    if len(pattern)>1 and pattern[1]=='*':
        # 如果字符串第一个 跟 模第一个字符匹配(相等或匹配到".")，可以有3种匹配方式：
        if s and (s[0]==pattern[0] or pattern[0]=='.'):
            # 模后移2，X*被忽略(*匹配0个字符)  match(s,pattern[2:])
            # 字符串移1，模移2(*匹配1个字符)   match(s[1:],pattern[2:])
            # 字符串移1，模不变(*匹配1个字符)  match(s[1:],pattern)
            return match(s, pattern[2:]) or match(s[1:],pattern[2:]) or match(s[1:],pattern)
        else:
            return match(s,pattern[2:])

    # 模第二个字符不是*
    # 如果字符串第一个字符和模式中的第一个字符匹配(相等或匹配到".")，那么字符串和模式都后移一个字符，然后匹配剩余的
    if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='.'):
        return match(s[1:],pattern[1:])
    return False

print(match('aaabbb','a.a*b*'))