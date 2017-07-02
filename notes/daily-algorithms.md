## 参考自 https://github.com/barretlee/daily-algorithms 
> 每日一题，想想都激动

## 17年

## 06-28

给定一个整数数组，其中有两项之和为一个特定的数字，假设每次 input 只有一个唯一解，不允许两次使用同一个元素，返回这两个数的索引。
比如：
给定 nums = [2, 7, 11, 15]，target = 9
由于 nums[0] + nums[1] = 9
所以返回 [0, 1]
> 参考答案:
借用对象字面量，对 ‘“是否存在另一个数” 与 “当前遍历的数” 之和为 target’ 这个问题进行判断。化 O(n^2) 为 O(n)
```javascript
var twoSum = function(nums, target) {
  var result = [];
  var map = {};
  var temp;
  for (var i = 0, len = nums.length; i < len; i++) {
      temp = target - nums[i];
      if (map[temp] !== undefined) {
          result[0] = parseInt(map[temp], 10) ;
          result[1] = i;
          return result;
      }
      map[nums[i]] = i;
  }
  return -1;
};
```
前提：
假设每次 input 只有一个唯一解
不允许两次使用同一个元素
 


