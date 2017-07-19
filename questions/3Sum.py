# -*- coding: utf-8 -*-

# 本题难度：★★
# 给定一个整数数组 S，找到所有的三元元组 (a, b, c)，使得 a + b + c = 0，注意，

# (a, b, c) 中 a ≤ b ≤ c
# 不要输出重复的元组
# 比如：

# 给定 S = [-1, 0, 1, 2, -1, -4]，输出 [[-1, 0, 1], [-1, -1, 2]]
# 参考答案：https://github.com/barretlee/daily-algorithms/blob/master/answers/12.md



# function resolve(list) {
#     var sortedList = list.sort(function(a, b) {
#         return (a < b ? -1 : a > b ? 1 : 0)
#     })
#     var result = [], LIST_LENGTH = sortedList.length, LAST_SECOND = LIST_LENGTH - 2

#     if (LIST_LENGTH >= 3) {
#         var first = 0, second = 1, inResult = {}, computing = true

#         while (computing) {
#             var a = sortedList[first], b = sortedList[second], v = [a, b].join()

#             for (var third = second + 1; third < LIST_LENGTH; third++) {
#                 var c = sortedList[third]

#                 if ((a + b > 0) || (a + b < 0 && c > -(a + b))) break

#                 if ((a + b + c === 0) && (inResult[c] !== v)) {
#                     inResult[c] = v
#                     result.push([a, b, c])
#                 }
#             }
#             if ((first < LIST_LENGTH - 3) && (second <= LAST_SECOND)) {
#                 second = (second === LAST_SECOND) ? (++first, first + 1) : ++second
#             } else {
#                 computing = false
#             }
#         }
#     }

#     return result
# }

# console.log(resolve([-1, 0, 1, 2, -1, 4]))

# Time Limit Exceeded 
def _3Sum(array):
    if len(array) < 3:
        return [];
    def _s(x,y):
        if x < y:
            return 1;
        elif x > y:
            return -1;
        else:
            return 0;
    # 妙点 1
    array.sort(_s);
    #print(array)
    ret = [];
    first,second = 0,1;
    flag = True;
    # 妙点2
    temp = {};
    while(flag):
        a = array[first];
        b = array[second];
        for third in range(second+1,len(array)):
            c = array[third];
            # 误区1
            if a+b < 0 or (a+b > 0 and a+b < -c):
                break;
            #print(a,b,c)
            if (a+b+c) == 0 and (temp.has_key(c) == False or  temp[c] != [a,b]):
                temp[c] = [a,b]
                ret.append([c,b,a]);
       
        # 误区2
        # first = second;
        # second = second +1;
        # if second > len(array)-2 :
        #     flag = False;
        if second == len(array)-2:
            if(first == second -1):
                flag = False;
            first = first +1;
            second = first +1;
        else:
            second = second  + 1 ;
    return ret; 

# print(_3Sum([-1, 0, 1, 2, -1, 4]))
# print(_3Sum([0, 0, 0,0, 0, 0]))
# print(_3Sum([0, 1, 1, 2, -1, -3]))
# print(_3Sum([-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,
# -12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,
# 10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8]))


## 方法2 Time Limit Exceeded
def _3Sum_1(array):
    if len(array) < 3:
        return [];
    def _s(x,y):
        if x < y:
            return -1;
        elif x > y:
            return 1;
        else:
            return 0;
    ret = [];
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums,target)
        for i in range(len(nums)):
            temp = target - nums[i];
            if temp in nums:
                # 注意重复值情形
                # tt = nums[i+1:]
                # print(tt)
                index = nums.index(temp);
                if index != i:
                    t = [nums[i],nums[index],-target];
                    t.sort(_s);
                    if t not in ret:
                        ret.append(t);
        return ret; 
    # 妙点 1
    array.sort(_s);
    
    for i in range(len(array)):
        if array[i] > 0:
            return ret;
        # 妙点1
        if i>=1 and array[i] == array[i-1]:
            continue;
        twoSum(array[i+1:],-array[i]);
    return ret;


# 重复值
#print(_3Sum_1([1,2,-2,-1]))
# 出现重复值时无法解决
#print(_3Sum_1([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
# 出现重复值时无法解决
#print(_3Sum_1([0,0,0]))

#print(_3Sum_1([0, 0, 0,0, 0, 0]))


# 思路一错，满盘皆输，思路最重要
def threeSum( nums ):
    # 经过 sorted 后其实已经排除了相同的可能
    nums = sorted(nums);
    print(nums);
    nums_len = len(nums);
    i = 0;
    ret = [];
    while (i < nums_len -2):
        a = nums[i];
        if a>0:
            return ret;
        # 误区1 nums[i] == nums[i+1]
        if nums[i] == nums[i-1]:
            i = i + 1;
            continue;
        m = i + 1;
        n = nums_len -1;
        while (m < n):
            b = nums[m];
            c = nums[n];
            if a + b + c < 0:
                m = m + 1;
                
            elif a + b + c > 0:
                n = n -1;
            else:
                ret.append([a,b,c]);
                m = m + 1;
                n = n -1;
                # 误区2 nums[m] == nums[m+1] / nums[n] == nums[n-1]
                while nums[m] == nums[m-1] and m +1 < n:
                    m = m +1;
                while nums[n] == nums[n+1] :
                    n = n -1;
        i = i +1;
    return ret

print(threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
# print(threeSum([0, 0, 0,0, 0, 0]))
