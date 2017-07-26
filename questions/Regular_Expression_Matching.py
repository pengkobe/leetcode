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

def Regular_Expression_Matching(str,patt):
    if not str and not patt:
        return True;
    if not str and not patt.replace("*",""):
        return True;
    if not str or not patt:
        return False;

    if patt and patt[0]=="*":
        return Regular_Expression_Matching(str[1:],patt) or Regular_Expression_Matching(str,patt[1:]);
    else:
        return (str[0]==patt[0] or patt[0] ==".") and Regular_Expression_Matching(str[1:],patt[1:]);


if __name__ == '__main__':
    assert Regular_Expression_Matching('aa', 'a') == False
    assert Regular_Expression_Matching('aa', 'aa') == True
    assert Regular_Expression_Matching('aaa', 'aaa') == True
    assert Regular_Expression_Matching('aaa', '.a') == False
    assert Regular_Expression_Matching('aa', '.*') == True
    assert Regular_Expression_Matching('aab', '*') == True
    assert Regular_Expression_Matching('b', '.*.') == False

