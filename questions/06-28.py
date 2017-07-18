# -*- coding: utf-8 -*-

# 本题难度：★
# 给定一个整数数组，其中有两项之和为一个特定的数字，假设每次 input 只有一个唯一解，不允许两次使用同一个元素，返回这两个数的索引。

# 比如：

# 给定 nums = [2, 7, 11, 15]，target = 9

# 由于 nums[0] + nums[1] = 9
# 所以返回 [0, 1]

# 标准答案
# var twoSum = function(nums, target) {
#   var result = [];
#   var map = {};
#   var temp;
#   for (var i = 0, len = nums.length; i < len; i++) {
#       temp = target - nums[i];
#       if (map[temp] !== undefined) {
#           result[0] = parseInt(map[temp], 10) ;
#           result[1] = i;
#           return result;
#       }
#       map[nums[i]] = i;
#   }
#   return -1;
# };


## 问题延伸到三个数之和

### 方案1
# const threeSum = (nums, target) => {
#   nums = nums.sort((x, y) => x - y);
  
#   const len = nums.length;
#   for (let fixedIndex = 0; fixedIndex < len - 2; ++fixedIndex) {
#     const requireSum = target - nums[fixedIndex];
    
#     let begin = fixedIndex + 1;
#     let end = len - 1;
#     while (begin !== end) {
#       const tempSum = nums[begin] + nums[end];
#       if (tempSum === requireSum) {
#         return [fixedIndex, begin, end];
#       } else if (tempSum < requireSum) {
#         ++begin;
#       } else {
#         --end;
#       }
#     }
#   }

#   return -1;
# }



### 方案2
# @szu-bee 也可以利用下 TwoSum 来处理：
# const threeSum = (input, target) => {

#   let i, len;
#   const hashMap = input.reduce((map, item, index) => {
#     if (!map[item]) map[item] = index;
#     return map;
#   }, {});

#   for (i = 0, len = input.length; i < len - 2; i++) {
#     const result = TwoSum(input.slice(i + 1), target - input[i], i + 1);
#     if (result !== -1) {
#       result.unshift(i);
#       return result;
#     }
#   }
#   return -1;

#   function TwoSum(input, target2, offset) {
#     for (let i = 0, len = input.length; i < len; i++) {
#       if (hashMap[target2 - input[i]] && input[i] !== target2 - input[i]) {
#         return [i + offset, hashMap[target2 - input[i]]];
#       }
#     }
#     return -1;
#   }

# };
# 算法有意思的地方有两点，一是可以不断优化，二是需要考虑各种边界条件。

## 三数相加为定值
def threeSum(input,target):
    map = {};
    
    for k,v in enumerate(input):
    	map[v] = k;
    
    ## 两数相加为定值
    def sumOfTwo(input,target2,startIndex):
        # for i in range(len(input)):
        # map[input[i]] = i;
        for i in range(len(input)):
              temp = target2 - input[i];
              if map[temp] and map[temp]>startIndex and map[temp] != i+startIndex:  
                  return [i+startIndex,map[temp]];
        return -1;

    for i in range(len(input)-1):
        temp = target - input[i];
        arraypart = input[i+1:];
        ret = sumOfTwo(arraypart, temp,i+1);
        if ret != -1:
            return [i] + ret;


print (threeSum([1,2,3,1,5,7,6],9))



# 两数相加为定值
def sumOfTwo(nums,target):
    map = {};
    # 不能存在重复值，失败
    for k,v in enumerate(nums):
        map[v] = k;
    for i in range(len(nums)):
        temp = target - nums[i];
        if map[temp] and map[temp] != i:
            return [i,map[temp]];
    return -1;

## 正解
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = target - nums[i];
            if temp in nums:
                index = nums.index(temp);
                if index != i:
                    return [i,index];
        return -1; 