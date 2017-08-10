# -*- coding: utf-8 -*-
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


## 解法1，自认思路没有问题，但是字符串前面有 + U
def isValid(s):
    ret = [];
    len_s = len(s) -1;
    while len_s > 0:
        if len(ret)==0 or ret[len(ret)-1] != s[len_s]:
            ret.append(s[len_s])
        else:
            ret.pop();
        len_s -= 1;
    if len(ret) == 0:
        return True;
    else:
        return False;
    return s;


# 解法2
def isValid2(s):
    if s == "":
        return True;
    ret = [None];
    strs = ["(",")","[","]","{","}"];
    for i in s:
        if i not in strs:
            return False;
        temp = strs.index(i);
        
        if ret[len(ret)-1] != strs[temp -1]:
            ret.append(i);
        else:
            if len(ret)>0:
                ret.pop();
    if len(ret)>0:
        ret.pop();
    return len(ret) == 0;
print(isValid2("a"))
print(isValid2("[]"))
print(isValid2("[{}]"))
print(isValid2("[{]"))
