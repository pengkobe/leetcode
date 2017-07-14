# -*- coding: utf-8 -*-

# 本题难度：★★
# 给定 N 个非负整数 a1, a2, ..., an, 每个数对应坐标上的一个点 (i, ai)，在坐标轴上将所有的 (i ,0) 和 (i, ai) 使用直线链接起来。

# 任何两条 相邻的 线 （包含 Y 轴） ，这两条线与 X 轴构成一个容器，找出容量最大的容器对应的线。

# 注意：不能够倾斜容器，并且 n 不小于 2。

# import math

# def Container_With_Most_Water(arr):
#     arrLen = len(arr);
#     maxArea = 0;
#     maxIndex = 0;
#     if(arrLen <= 2):
#         return 0;

#     for i in range(arrLen-1):
#         if i ==0:
#             maxArea = arr[i][0] * arr[i][1];
#         else:
#             height = arr[i][1] if arr[i][1] < arr[i+1][1] else  arr[i+1][1];
#             area = height * (arr[i+1][0] - arr[i][0]);
#             area = area if area > 0 else  -1 * area;
#             print(area)
#             if area > maxArea:
#                 maxArea = area;
#                 maxIndex = [arr[i],arr[i+1]]
#     return maxIndex;

# print(Container_With_Most_Water([[1,3],[2,1],[3,5]]));



# import math

# def Container_With_Most_Water(arr):
#     arrLen = len(arr);
#     maxArea = 0;
#     maxIndex = 0;
#     if(arrLen <= 2):
#         return 0;

#     for i in range(arrLen-1):
#         if i ==0:
#             maxArea = 1 * arr[i];
#         else:
#             height = arr[i] if arr[i] < arr[i+1] else  arr[i+1];
#             area = height * 1;
#             area = area if area > 0 else  -1 * area;
#             print(area)
#             if area > maxArea:
#                 maxArea = area;
#                 maxIndex = [i,i+1]
#     return maxIndex;

# print(Container_With_Most_Water([3, 4, 3, 8, 2, 7, 9]));



# Time Limit Exceeded
# def Container_With_Most_Water(arr):
#     maxArea = 0;
#     arrLen = len(arr);
#     for i in range(arrLen):
#         for j in range(i+1,arrLen):
#             height = arr[i] if arr[i] < arr[j] else  arr[j];
#             if maxArea < height * (j - i):
#                 maxArea =  height * (j - i)

#     return maxArea
# print(Container_With_Most_Water([3, 4, 3, 8, 2, 7, 9]));

# 听说有点类似夹逼算法
def Container_With_Most_Water(arr):
    maxArea = 0;
    arrLen = len(arr);
    i,j = 0,arrLen -1;
    while (i < j):
        height = arr[i] if arr[i] < arr[j] else  arr[j];
        maxArea = max(maxArea, height*(j-i));
        if arr[i] < arr[j]:
            i +=1;
        else:
            j -=1;
    return maxArea;


print(Container_With_Most_Water([3, 4, 3, 8, 2, 7, 9]));
