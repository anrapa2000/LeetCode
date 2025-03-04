/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  end = nums.length - 1;
  start = 0;
  while (start <= end) {
    mid = Math.floor((end + start)/2)
    if (nums[mid] === target) {
        return mid
    }
    else if (nums[mid] < target) {
      start = mid + 1;
    }
    else{
      end = mid - 1;
    }
  }
  return -1;
};

const nums = [-1, 0, 3, 5, 9, 12],
  target = 9;
console.log(search(nums, target)); // 4
