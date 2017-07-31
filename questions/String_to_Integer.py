# -*- coding: utf-8 -*-
# Add to List
# 8. String to Integer (atoi)
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

# spoilers alert... click to show requirements for atoi.

# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


# 考虑事项
# 1. 开头为 + - 号
# 2. 只有 + - 号
# 3. str 为空
# 4. str 为非法字符串
# 5. str 超过最大值与最小值
# 6. 如何对空格进行友好的处理

def myAtoi(str):
    ret = 0;
    INT_MAX = 2147483647;  
    INT_MIN = -2147483648;
    a_0 = ord('0')  
    a_9 = ord('9')    
    belowZero =False;
    if str == "":
        return False;
    str_len = len(str);
    # 去掉前半部分空格
    i= 0;
    while i < str_len and str[i] == ' ':  
        i += 1 
    str =str[i:];
    str_len = len(str);

    # 符号位判断
    if str[0]=="-":
        belowZero = True;
    if str[0] == "+" or str[0]=="-":
        str = str[1:];
        str_len -=1;
    if str_len == 0:
        return False;

    # change to number
    for i in range(str_len):
        # 剔除特殊字符串
        if ord(str[i]) < a_0 or ord(str[i]) > a_9:
            return False;
        else:
            #print('ret',ret,'stri',str[i],'belowZero0',belowZero)
            # 对最值进行判断
            if ret > INT_MAX / 10 or ( ret == INT_MAX/10 and ord(str[i])-a_0 > 7):
                if belowZero:
                    if ord(str[i])-a_0 > 8:
                        return False
                else:
                    return False;
            ret = 10*ret + ord(str[i]) - a_0;
            
            
 
    if belowZero:
        return -ret;
    return ret;
print(myAtoi('')); 
print(myAtoi('  123'));  
print(myAtoi('aa')); 
print(myAtoi('-aaa'));     
print(myAtoi('-0'));
print(myAtoi('2147483647'));
