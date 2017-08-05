# -*- coding: utf-8 -*-

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

## 参考答案(别人的解法真牛)：https://leetcode.com/problems/4sum/discuss/
# def fourSum(self, nums, target):
#     def findNsum(nums, target, N, result, results):
#         if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
#             return
#         if N == 2: # two pointers solve sorted 2-sum problem
#             l,r = 0,len(nums)-1
#             while l < r:
#                 s = nums[l] + nums[r]
#                 if s == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     while l < r and nums[l] == nums[l-1]:
#                         l += 1
#                 elif s < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else: # recursively reduce N
#             for i in range(len(nums)-N+1):
#                 if i == 0 or (i > 0 and nums[i-1] != nums[i]):
#                     findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

#     results = []
#     findNsum(sorted(nums), target, 4, [], results)
#     return results

def fourSum(nums, target):
    nums_len = len(nums);
    if nums_len < 4:
        return [];
    nums = sorted(nums);
    i = 0;
    res = [];


    def threeSum( nums,target ):
        # 妙点: 排序后，可以降低比对的难度
        nums_len = len(nums);
        i = 0;
        ret = [];
        while (i < nums_len -2):
            a = nums[i];
            # 误区1 nums[i] == nums[i+1]
            if i!=0 and nums[i] == nums[i-1]:
                i = i + 1;
                continue;
            m = i + 1;
            n = nums_len -1;
            while (m < n):
                b = nums[m];
                c = nums[n];
                print(a,b,c,target)
                if a + b + c < target:
                    m = m + 1;
                    
                elif a + b + c > target:
                    n = n -1;
                else:
                    ret.append([a,b,c]);
                    m = m + 1;
                    n = n -1;
                    # 误区2 nums[m] == nums[m+1] / nums[n] == nums[n-1]
                    while nums[m] == nums[m-1] and m +1 < n:
                        m = m +1;
                    while n > 0 and nums[n] == nums[n+1] :
                        n = n -1;
            i = i +1;
        return ret


    while i < nums_len:
        if i > 0 and nums[i] == nums[i -1]:
            i +=1;
            continue;
        else:
            #print("nums[i+1:]",nums[i+1:])
            ret = threeSum(nums[i+1:],target-nums[i]);
            if len(ret) == 0:
                i +=1;
                continue;
            else:
                #print("ret",ret)
                for j in range(len(ret)):
                    res.append([nums[i]]+ret[j]);
        i +=1;
            
    return res;


#print(fourSum([1,2,3,4,0,1,5],10))
# print(fourSum([0,0,0,0],0))
# [[0,4,4,4],[2,2,4,4]]
print(fourSum([0,4,-5,2,-2,4,2,-1,4],12))


