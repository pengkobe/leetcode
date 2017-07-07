# -*- coding: utf-8 -*-

# 本题难度：★★
# 找出一个字符串中最长的连续子串，输出这个子串的长度，要求：这个子串中没有重复的字符。

# 比如：

# 给定 abcabcbb，最长的子串为 abc，那么输出结果为 3;
# 给定 bbbbb，最长的子串是 b，输出结果为 1;
# 给定 pwwkew，最长的子串为 wke，输出 3.
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/4.md


# function longestUniqueSubstr (str) {
#   str = String(str)

#   var index = {} // keys: char of a tentative substr, values: index
#   var tenLen = 0 // len of the tentative substr

#   var resLen = 0 // result len

#   for (let i = 0; i < str.length; i += 1) {
#     let ic = index[str[i]]
#     if (typeof ic !== 'undefined') {
#       if (tenLen > resLen) { resLen = tenLen }
#       i = ic + 1
#       index = {}
#       tenLen = 0
#     }
#     index[str[i]] = i
#     tenLen += 1
#   }

#   return Math.max(tenLen, resLen)
# }

def longestUniqueSubstr(s):
    substr = []
    maxStrlen = 1;
    for i in range(len(s)):
        if s[i] in substr:
            index = substr.index(s[i])
            if maxStrlen < len(substr):
                maxStrlen = len(substr)
            substr = substr[index+1:]
        substr.append(s[i])
    return len(substr) if len(substr) > maxStrlen else maxStrlen;

print(longestUniqueSubstr('bpfbhmipx'))