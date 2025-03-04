/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let array = [];
  let map = {};
  nums.sort((a, b) => a - b);
  console.log("nums", nums);
  for (let i = 0; i < nums.length; i++) {
    let target = -nums[i];
    let j = i + 1;
    let k = nums.length - 1;
    while(j < k){
        if(nums[j] + nums[k] === target){
            array.push([nums[i], nums[j], nums[k]]);
        }
        else if(nums[j] + nums[k] < target){
            j++
        }
        else{
            k--
        }
    }
  }
  return array;
};

const result = threeSum([-1, 0, 1, 2, -1, -4]);
console.log(result);
