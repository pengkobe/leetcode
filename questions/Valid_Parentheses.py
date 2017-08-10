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
    ret = [];
    strs = ["(",")","[","]","{","}"];
    
    return len(ret) > 0;
