# -*- coding: utf-8 -*-

# Implement int sqrt(int x).
# Compute and return the square root of x.

## 参考答案 http://blog.csdn.net/ithomer/article/details/8777088

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x;
    t_high = x;
    t_mid = x/2
    t_low = 1;
    while (t_high-t_low) > 1:
        if t_mid*t_mid > x:
            t_high = t_mid;
        else:
            if t_mid*t_mid == x:
                return t_mid;
            t_low = t_mid;
        t_mid = (t_low+t_high)/2;
            
    return t_low;



print(mySqrt(29)) 


        
