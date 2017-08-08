# -*- coding: utf-8 -*-
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

def median(nums1, nums2):
    def getKth(A,B,kth):
        print('getKth',A,B,kth)
        if len(A) > len(B):
            return getKth(B,A,kth);
        if len(A) == 0:
            return B[kth-1];
        if kth == 1:
            return min(A[0],B[0]);

        pa = min(len(A), kth/2);
        pb = kth - pa;
        if A[pa-1] <= B[pb-1]:
            return getKth(A[pa:],B,pb);
        else:
            return getKth(A,B[pb:],pa);        

    len_nums1 = len(nums1);
    len_nums2 = len(nums2);
        
    t_len = len_nums1 + len_nums2;
    if t_len % 2 == 1:
         return getKth(nums1,nums2,t_len/2 +1 );
    else:
        # /2 必须改为 * 0.5 否则四舍五入不会准的！！！！
        return (getKth(nums1,nums2,t_len/2 +1 ) + getKth(nums1,nums2,t_len/2 )) /2;

print(median([1, 3],[2]))
print(median([2],[0]))
print(median([2],[]))