# -*- coding: utf-8 -*-

# 本题难度：★★
# 两个非空链表，分别代表两个非负整数，链表的每个节点储存着整数的一位，并且是倒序储存的，将这两个数字相加返回新的链表，如：

# 输入: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 返回: 7 -> 0 -> 8
# 提示，这道题需要考虑溢出问题。

def addLinkedList(a,b):
    addflag = 0 ;
    len_a = len(a);
    len_b = len(b);
    if(len_a == len_b == 0):
        return [];
    ret = [];

    min_len = len_a if len_a < len_b else len_b;
    for i in range(min_len):
        value = a[i] + b[i];
        if addflag == 1:
            value = value + addflag;
        if value >= 10:
            addflag = 1;
            value -= 10;
        else:
            addflag = 0;
        ret.append(value);
    
    temp = a if len_a > len_b else b;
    max_len = len_a if len_a > len_b else len_b;
    for j in range(min_len, max_len):
        if addflag == 1:
             temp[j] =  temp[j] + addflag;
        if temp[j] >= 10:
            addflag = 1;
            temp[j] -= 10;
        else:
            addflag = 0;
            break;
    if addflag == 1:
        temp.append(1);
    ret = ret + temp[min_len:];
        
    return ret;

print (addLinkedList([2,4,3],[5,6,4]))
print (addLinkedList([2,4,3,9,9],[5,6,9]))