# -*- coding: utf-8 -*-
# 本题难度：★★
# 找到字符串 s 中最长的连续回文串，假定 s 的最大长度为 1000，如

# 输入 "babad"，输出 "bab"，"aba" 也是正确答案
# 输入 "cbbd"，输出 "bb"
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master


def Find_The_Longest_Palindromic_Substring(str):
    strlen = len(str);
    D = [[0]* strlen for i in range(strlen)]  
    for i in range(strlen):
        D[i][i] = True;
        if i < strlen-1:
            D[i][i+1] = True;
    
     for i in range(2,strlen):
          for j in range(0,strlen-i):
              if(D[i][j] && str[j] = str[j + i -1]):
                  

    
    

Find_The_Longest_Palindromic_Substring('xxasd')