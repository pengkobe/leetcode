# -*- coding: utf-8 -*-
# 本题难度：★
# 给定一个罗马数字（1~3999），将其转换为整数。

# 例如罗马数字 MCDXXXVII 对应数字为：1437。

# 相关资料：#9
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/10.md

def Roman_To_Integer(rm):
    map = {
    'M': 1000, 
    'D': 500, 
    'C': 100,
    'L': 50, 
    'X': 10,
    'V': 5, 
    'I': 1
    };
   
    rmLen = len(rm);
    ret = 0;
    for i in range(rmLen):
        if i+1 < rmLen:
            ret += map[rm[i]] * (1 if map[rm[i]] >= map[rm[i+1]] else -1);

    return ret + map[rm[rmLen-1]];


print(Roman_To_Integer('MCDXXXVII'))
print(Roman_To_Integer('CMXCIX'))