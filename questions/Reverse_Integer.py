# -*- coding: utf-8 -*-
# 2017-06-29
# 本题难度：★
# 将一个 32-bit 无符号整数的所有数字倒序，输出一个新的整数，如

# eg1. x = 123, return 321
# eg2. x = -123, return -321
# 提示：

# 考虑末尾为零的情况，如 10, 100
# 考虑溢出情况，如将 1000000003 倒序排列
# 溢出则输出 0.

import sys
import math

def reverseInteger(x):
    res = 0
    flag = lambda x:x<0
    flag = flag(x)
    x = abs( x )
    maxint = math.pow(2, 31)-1
    print(maxint)
    # 使用这个在 leetcode 环境下会报错
    print(sys.maxint)
    while 1:
        if x == 0:
            break
        res = res * 10 + x % 10
        if res > maxint :
            return 0
        x = x/10
    if(flag):
        return -res
    else:
        return res
      
print("123",reverseInteger(123))
print("-123",reverseInteger(-123))
print("100",reverseInteger(100))
print("1534236469",reverseInteger(1534236469))
print("1563847412",reverseInteger(1563847412))


## 其它方案
# class Solution {
# public:
#     int reverse(int x) {
#         long long res = 0;
#         while (x != 0) {
#             res = 10 * res + x % 10;
#             x /= 10;
#         }
#         return (res > INT_MAX || res < INT_MIN) ? 0 : res;
#     }
# };
