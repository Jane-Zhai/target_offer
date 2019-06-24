"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长字符串的长度。假设字符串中只包含‘a’-‘z’的字符。例如，在字符串“arabcacfr”中，最长的不含重复字符的子字符串是“acfr”，长度为4。
"""
def longestStr(s):
    start = 0
    length = 0
    used = dict()
    for i,word in enumerate(s):
        if word in used:# and start<=used[word]:
            start = used[word] + 1
        else:
            length = max(length,i-start+1)
        used[word] = i

    return length

print(longestStr('pwwkew'))

