/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i = 0; i< nums.length; i++){
        let number = target - nums[i];
        if(nums.includes(number) && nums.indexOf(number) !== i){
            return [i, nums.indexOf(number)];
        }
    }
};

// console.log(twoSum([2,7,11,15], 9)); // [0, 1]
// console.log(twoSum([3,2,4], 6)); // [0, 1]
// console.log(twoSum([3,3], 6)); // [0, 1]