# -*- coding: utf-8 -*-

# 本题难度：★★
# 给一个整数（1~3999），将其转换为罗马数字。

# 罗马字符	I	V	X	L	C	D	M
# 对应数字	1	5	10	50	100	500	1000
# 例如整数 1437 对应罗马数字为：MCDXXXVII。

# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/9.md


def Integer_To_Roman(num):
    map = [
        ['', "M", "MM", "MMM"],
        ['', "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ['', "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ['', "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ];
    ret = '';
    flag = 1;
    while num >0:
        d = num % 10;
        ret = map[4-flag][d] + ret;
        num = num/10;
        flag = flag+1;

    return ret;
        
print(Integer_To_Roman(1437))
print(Integer_To_Roman(1000))
print(Integer_To_Roman(1001))
print(Integer_To_Roman(1))