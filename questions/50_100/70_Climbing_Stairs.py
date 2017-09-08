# -*- coding: utf-8 -*-

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Time Limit Exceeded 
# def climbStairs1(n):
#     if n<=2:
#         return n;
#     else:
#         return climbStairs1(n-1)+climbStairs1(n-2) +2;

# print(climbStairs1(5))


def climbStairs(n):
   if n<=2:
       return n;
   n_1 = 2;
   n_2 = 1;
   ret = 0;
   for i in range(3,n+1):
       ret = n_1 +  n_2;
       n_2 = n_1;
       n_1 = ret;
   return ret;
print(climbStairs(35))