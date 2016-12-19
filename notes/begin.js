/**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    let n = nums.length;
    this.nums = nums;
    this.sumToNumber = [nums[0]];
    for(let i = 1; i < n; i++){
        this.sumToNumber[i] = nums[i] + this.sumToNumber[i-1];
    }
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    if(i === 0){
        return this.sumToNumber[j];
    }else {
        return this.sumToNumber[j] - this.sumToNumber[i-1];
    }
};