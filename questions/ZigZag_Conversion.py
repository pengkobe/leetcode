# -*- coding: utf-8 -*-
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

## 只转换 3 的版本
def convert(str, row):
    str_len = len(str);
    column = str_len / 4;
    left = str_len % 4;
    i = 0;
    ret = "";
    ret1 = "";
    ret2 = "";
    ret3 = "";

    while i < column:
        ret1 += str[4*i];
        ret2 += str[4 * i + 1] +str[4 * i + 3];
        ret3 += str[4 * i + 2];
        i += 1;
    
    if left == 1:
        ret1 += str[4 * i];
    elif left == 2:
        ret2 += str[4 * i+ 1];
    elif left == 3:
        ret3 += str[4 * i+ 2];
    else:
        pass;

    ret = ret1+ret2+ret3;
    return ret;


#print(convert("PAYPALISHIRING",3))


def convert2(str, row):
    if row == 1:
        return str;
    str_len = len(str);
    base = row + row/2;
    # 注意多加 1 列
    column_base = str_len / base ;
    column = (column_base + 1) * 2;
    result_arr = [['' for i in range(column)] for j in range(row)]
    left = str_len % base;
    i = 0;
    while i < column_base:
        j = 0;
        while j < row:
            if j % 2 ==1:
                result_arr[j][2 * i] = str[base * i + j];
                result_arr[j][2 * i+1] = str[base * i + j * 2 + 1];
            else:
                result_arr[j][2 * i] = str[base * i + j];
            j +=1;
        i += 1;

    # 处理 left
    j = 0;
    while j < left and j < row:
        if j % 2 ==1:
            result_arr[j][2 * i] = str[base * i + j];
            if (base * i + j * 2 + 1) < str_len:
                result_arr[j][2 * i+1] = str[base * i + j * 2 + 1];
        else:
            result_arr[j][2 * i] = str[base * i + j];
        j += 1;
    return result_arr;


print(convert2("PAYPALISHIRING",3))