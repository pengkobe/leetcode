# -*- coding: utf-8 -*-
# 本题难度：★
# 不使用额外储存空间，判断一个整数是否为回文数字。例如：

# -22 -> false
# 1221 -> true
# 1221221 -> true
# 1234321 -> true
# 234 -> false
# 需要注意的是：

# 考虑负数
# 不允许使用额外储存空间，比如将数字转换成字符串
# 反转数字需要考虑溢出问题
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/7.md

import math

def Palindrome_Number(num):
    if num < 0:
        return False;
    # 计算数字所拥有的位数
    LenOfNum = 0;
    while(10**LenOfNum <= num):
        LenOfNum = LenOfNum+1;
    if LenOfNum == 1:
        return True;
    while(LenOfNum >= 2):
        a = num % 10;
        b = num / 10**(LenOfNum-1);
        if (a == b):
            num = num % (10**(LenOfNum-1))
            num = num /10;
            LenOfNum -= 2;
        else:
            return False;
    return True;

print(Palindrome_Number(10))
print(Palindrome_Number(1))
print(Palindrome_Number(-22))
print(Palindrome_Number(1221))
print(Palindrome_Number(1221221))
print(Palindrome_Number(1234321))
print(Palindrome_Number(234))