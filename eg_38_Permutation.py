'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
def permutation(ss):
    if not len(ss):
        return []
    if len(ss) == 1:
        return list(ss)

    lis = list(ss)
    lis.sort()
    p = []
    for i in range(len(lis)):
        if i > 0 and lis[i] == lis[i-1]:
            continue
        temp = permutation(''.join(lis[:i])+''.join(lis[i+1:]))
        for j in temp:
            p.append(lis[i]+j)
    return p

print(permutation('abc'))