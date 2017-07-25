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

def Regular_Expression_Matching():
    return ;