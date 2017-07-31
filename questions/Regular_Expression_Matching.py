# -*- coding: utf-8 -*-
# 本题难度：★★★
# 实现一个正则表达式引擎，让其支持匹配 . 和 *，其中：

# . 匹配任何单字符
# * 匹配 0 个或者多个前字符
# 需要匹配全部输入而非部分输入，函数格式如下：

# bool isMatch(const char *s, const char *p)
# 如：

# isMatch('aa', 'a') // false
# isMatch('aa', 'aa') // true
# isMatch('aaa', 'aa') // false
# isMatch('aa', 'a*') // true
# isMatch('aa', '.*') // true
# isMatch('ab', '.*') // true
# isMatch('aab', 'c*a*b') // true
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/6.md


# Wrong Anwer1
# def isMatch(_str,patt):
#     if not _str and not patt:
#         return True;
#     if not _str and not patt.replace("*",""):
#         return True;
#     if not _str or not patt:
#         return False;
#   此处与题目要求不符
#     if patt and patt[0]=="*":
#         return isMatch(_str[1:],patt) or isMatch(_str,patt[1:]);
#     else:
#         return (_str[0]==patt[0] or patt[0] ==".") and isMatch(_str[1:],patt[1:]);


# if __name__ == '__main__':
#     assert isMatch('aa', 'a') == False
#     assert isMatch('aa', 'aa') == True
#     assert isMatch('aaa', 'aaa') == True
#     assert isMatch('aaa', '.a') == False
#     assert isMatch('aa', '.*') == True
#     assert isMatch('aab', '*') == True
#     assert isMatch('b', '.*.') == False
#     assert isMatch('aab', 'c*a*b') == True


# 提交解法1 备份
# class Solution(object):
#     def isMatch(self, _str, patt):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if len(patt)==0: 
#             return len(_str)==0

#         if len(patt)>1 and patt[1]=="*":
#             i = 0;
#             if len(_str) ==0:
#                 if self.isMatch(_str[0:],patt[2:]):
#                     return True;
#             while i < len(_str):
#                 if i == 0 and self.isMatch(_str[0:],patt[2:]):
#                         return True;
#                 if _str[i] ==patt[0] or patt[0] ==".":
#                     if self.isMatch(_str[i+1:],patt[2:]):
#                         return True;
#                 else:
#                     break;
#                 i = i +1;
#             return False;
#         else:
#             if _str and (_str[0]==patt[0] or patt[0] =="."):
#                 return self.isMatch(_str[1:],patt[1:]);
#             else:
#                 return False;

# 解法1
def isMatch2(_str,patt):
    if len(patt)==0: 
        return len(_str)==0

    if len(patt)>1 and patt[1]=="*":
        i = 0;
        if len(_str) ==0:
            if isMatch2(_str[0:],patt[2:]):
                return True;
        while i < len(_str):
            if i == 0 and isMatch2(_str[0:],patt[2:]):
                return True;
            if _str[i] == patt[0] or patt[0] ==".":
                if isMatch2(_str[i+1:],patt[2:]):
                    return True;
            else:
                break;
            i = i +1;
        return False;
        
    else:
        print('else',_str[0:]);
        if _str and (_str[0]==patt[0] or patt[0] =="."):
            return isMatch2(_str[1:],patt[1:]);
        else:
            return False;


if __name__ == '__main__':
    assert isMatch2('aa', 'a') == False
    assert isMatch2('aa', 'aa') == True
    assert isMatch2('aaa', 'aaa') == True
    assert isMatch2('aaa', '.a') == False
    assert isMatch2('ab', '.*') == True
    assert isMatch2('aa', '.*') == True
    assert isMatch2('b', '.*.') == True
    assert isMatch2('aab', 'c*a*b') == True
    assert isMatch2('aaba', 'ab*a*c*a') == False
    assert isMatch2('a', '.*..a*') == False
    assert isMatch2('a', 'ab*') == True
    assert isMatch2('abcd', 'd*') == False
    assert isMatch2('ab', '.*c') == False

## 解法1 参考
# def isMatch3( s, p):
#     if len(p)==0: 
#         return len(s)==0
#     if len(p)==1 or p[1]!='*':
#         if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
#             return False
#         return isMatch3(s[1:],p[1:])
#     else:
#         i=-1; 
#         length=len(s)
#         while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
#             print(length,i+1,s[i+1:]);
#             if isMatch3(s[i+1:],p[2:]): 
#                 return True
#             i+=1
#         return False


## 动态规划的解法
## 思路推演
# 1. 全部初始化为 False 先，这里用二位数组 dp[i][j] 标识， 即 s 中前 r 个字符与 p 中前 j 个字符是否匹配
# 2. dp[0][0]=True，空字符配空字符，恒为 True
# 3. s 为空字符，考虑 x* 号情形，注意，按题目要求，*前必须有一个非*字符
# 4. 正式开始规划
#    1. 为 .
#    2. 为 * （难点）
#    3. 为普通字符

# @return a boolean
def isMatch4(s, p):
    s_len = len(s);
    p_len = len(p);
    dp = [[False for j in range(p_len+1)] for i in range(s_len+1)];
    dp[0][0] = True;
    for i in range(2,p_len+1):
        if p[i-1] == "*":
            dp[0][i] = dp[0][i-2];

    for i in range(1,s_len+1):
        for j in range(1,p_len+1):
            if p[j-1] == ".":
                dp[i][j] = dp[i-1][j-1];
            elif p[j-1] == "*":
                # 误点1. p[i-2]=="."
                # 误点2 . dp[i-1][j-1] --> dp[i-1][j]
                dp[i][j] = dp[i][j-1] or dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2]==".") and dp[i-1][j]);
            else:
                dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j -1]);

    return dp[s_len][p_len];

if __name__ == '__main__':
    assert isMatch4('aa', 'a') == False
    assert isMatch4('aa', 'aa') == True
    assert isMatch4('aaa', '.a') == False
    assert isMatch4('ab', '.*') == True
    assert isMatch4('aa', '.*') == True
    assert isMatch4('b', '.*.') == True
    assert isMatch4('aab', 'c*a*b') == True
    assert isMatch4('aaba', 'ab*a*c*a') == False
    assert isMatch4('a', '.*..a*') == False
    assert isMatch4('a', 'ab*') == True
    assert isMatch4('abcd', 'd*') == False
    assert isMatch4('ab', '.*c') == False
    assert isMatch4('abc', 'a*c') == False
    #  dp[i-1][j-1] --> dp[i-1][j], 举例如 aa vs .
    assert isMatch4('aaa', '.*') == True
