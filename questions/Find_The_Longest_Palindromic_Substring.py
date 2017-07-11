# -*- coding: utf-8 -*-
# 本题难度：★★
# 找到字符串 s 中最长的连续回文串，假定 s 的最大长度为 1000，如

# 输入 "babad"，输出 "bab"，"aba" 也是正确答案
# 输入 "cbbd"，输出 "bb"
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master


## 此处使用递归法解答
def Find_The_Longest_Palindromic_Substring(s):
    strlen = len(s);
    leftIndex, rightIndex = 0,0;
    D = [[False]* strlen for i in range(strlen)]  
    for i in range(0,strlen-1):
        D[i][i] = True;
        if i < strlen-1:
            #print(s[i])
            if(s[i] == s[i+1]):
                D[i][i+1] = True;
                rightIndex = i+1;
                leftIndex = i;
    
    for i in range(1,strlen):
        #print ('range1',i) 
        for j in range(0,strlen-i):
            #print ('range2',j) 
            if (D[j+1][j+i-1] and s[j] == s[j+i]):
                D[j][j+i] = True;
                if (rightIndex - leftIndex) < i:
                    leftIndex = j;
                    rightIndex= i+j;
                
    #print(leftIndex);
    #print(rightIndex);
    return s[leftIndex:rightIndex+1];
    
print(Find_The_Longest_Palindromic_Substring('vv'))
print(Find_The_Longest_Palindromic_Substring('saxxasd'))
print(Find_The_Longest_Palindromic_Substring('cbbd'))
print(Find_The_Longest_Palindromic_Substring('babad'))