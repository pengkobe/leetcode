# -*- coding: utf-8 -*-
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
#  from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

## 2min 答案
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ret = [];
        i = 0;
        j = 0;
        while i < m and j < n:
            if nums1[i] >= nums2[j]:
                ret.append(nums1[i]);
                i +=1;
            else:
                ret.append(nums2[j]);
                j +=1;
        if i<m:
            for m in range(i,m):
                ret.append(nums1[m]);
        if j<n:
            for m in range(i,m):
                ret.append(nums2[m]);
        nums1 = ret;

## 参考答案（读懂题意有多重要在）
class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a,b,k = m-1,n-1,m+n-1;
        while a>=0 and b>=0:
            if nums1[a] > nums2[b]:
                nums1[k] = nums1[a];
                a,k = a-1,k-1;
            else:
                nums1[k] = nums2[b];
                b,k = b-1,k-1;
        
        if b>=0:
            nums1[:b+1] = nums2[:b+1];
        
