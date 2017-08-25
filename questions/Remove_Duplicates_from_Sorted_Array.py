# -*- coding: utf-8 -*-

# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

# 误解题意，以为只要返回长度
# def removeDuplicates(nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         num_len = len(nums);
#         if num_len <=1:
#             return num_len;
#         count = 1;
#         ret = num_len;
#         while count < num_len:
#             if nums[count-1] == nums[count]:
#                 ret -=1;
#             count += 1;

#         return ret;


# print(removeDuplicates([1,1,1,2,2,2]))
# print(removeDuplicates([1,1,1,2]))


def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums);
        if num_len <=1:
            return num_len;
        pre,curr = 0,0;
        while curr < num_len:
            if nums[pre] == nums[curr]:
                curr+= 1;
            else:
                pre += 1;
                nums[pre] = nums[curr];
                curr +=1;

        return pre +1;


print(removeDuplicates([1,1,1,2,2,2]))
print(removeDuplicates([1,1,1,2]))