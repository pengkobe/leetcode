# -*- coding: utf-8 -*-

# 本题难度：★★
# 给定一个长度为 n 整数数组 S，找出三个整数，使得三数之和最接近给定的一个目标数 target，返回这三数之和。

# 假定给定的 S 只有一个解，例如：

# 给定 S = [-1, 2, 1, -4], target = 1，与 target 最接近的三数和为 (-1 + 2 + 1 = 2)，输出 2.


# 运行效率只击败了 17% 的用户
def threeSum_Closest( nums,target):
    # 妙点: 排序后，可以降低比对的难度
    nums = sorted(nums);
    nums_len = len(nums);
    i = 0;
    #ret = [];
    
    # 记录最小值, 误区1
    min_value = 0;
    m1 = abs(abs( nums[nums_len -1]) - abs(target))
    m2 = abs(abs( nums[0]) - abs(target))
    if m1 > m2:
        min_value = m1 * 3;
    else:
        min_value = m2 * 3;
    ret = min_value;
    while (i < nums_len -2):
        a = nums[i];
        if nums[i] == nums[i-1] and i>0:
            i = i + 1;
            continue;
        m = i + 1;
        n = nums_len -1;
        while (m < n):
            b = nums[m];
            c = nums[n];
            num_sum = a + b + c;
            d_minus = abs(num_sum - target)
           
            if (d_minus <= min_value):
                min_value = d_minus;
                ret = num_sum;
                #print(ret,[a,b,c])
            if  num_sum < target:
                m = m + 1;
            elif num_sum > target:
                n = n -1;
            else:
                return num_sum; 
        i = i + 1;
    return ret;

print(threeSum_Closest([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0], 5))

print(threeSum_Closest([7,5,4,-2,-7], 11))

print(threeSum_Closest([0,0,0], 1))

print(threeSum_Closest([1,1,1,0], -100))

