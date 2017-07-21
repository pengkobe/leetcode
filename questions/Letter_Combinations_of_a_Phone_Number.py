# -*- coding: utf-8 -*-
# 题目出处:https://github.com/barretlee/daily-algorithms/issues/15
# 本题难度:★★
# 给定一个纯数字的字符串，根据下面九宫格表返回所有可能的字母组合:

# 九宫格表

# 比如给定 "23"，那么所有可能的输出为:["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# 注意:上面给出的是按照辞典顺序输出的，可以不考虑顺序。
import copy;
def Letter_Combinations_of_a_Phone_Number(digits):
   words = {"0":" ","1":"*","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"};
   def concatStr(a,b):
       b = words[b];
       temp = [];
       if (a == []):
            for m in range(len(b)):
                temp.append(b[m]);
            
       for i in range(len(a)):
           for j in range(len(b)):
               temp.append(a[i]+b[j]);
       return temp;

   tt = reduce(concatStr,digits,[]);
   return tt;

print(Letter_Combinations_of_a_Phone_Number("00"))
print(Letter_Combinations_of_a_Phone_Number("12312"))

