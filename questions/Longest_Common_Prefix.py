# -*- coding: utf-8 -*-

# 本题难度：★
# 写一个函数，找出一个字符串数组的最长共同前缀。例如：

# 给定 ['hi, barret', 'hi, skylar', 'hi, john']，输出 'hi, '

# 注意事项:在 leetcode 中 字符串必须用 " 这个

def Longest_Common_Prefix(strs):
    arrLen  = len(strs);
    if(arrLen == 0):
        return '';
    temp = strs[0];
    for i in range(1,arrLen):
        j = 0;
        ret = "";
        #print('strs[i]:',strs[i])
        while j < len(temp) and j < len(strs[i]):
            #print('temp[j]:',temp[j])
            if temp[j] == strs[i][j]:
                ret = ret +  temp[j];
            else:
                break;
            j = j+1;
        #print('ret:',ret)
        temp = ret;
        if j ==0:
            break
        
    return temp;
                

print(Longest_Common_Prefix(["heel, xxx", "hello, skylar", "hei, john"]))
print(Longest_Common_Prefix(['heel, xxx']))
print(Longest_Common_Prefix(['aa', 'a']))
print(Longest_Common_Prefix(['a', 'b']))