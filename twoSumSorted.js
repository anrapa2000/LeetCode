/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  //   let array = [];
  //   for (let i = 0; i < numbers.length; i++) {
  //     let number = target - numbers[i];
  //     console.log(i, numbers.indexOf(number))
  //     if (numbers.includes(number) && numbers.indexOf(number) !== i) {
  //       array.push(i + 1);
  //       array.push(numbers.indexOf(number) + 1);
  //       return array;
  //     }
  //   }
  let array = [];
  let left = 0,
    right = numbers.length - 1;
  while (left < numbers.length) {
    let value = numbers[left] + numbers[right];
    if (value === target) {
      array.push(left + 1);
      array.push(right + 1);
      return array;
    } else if (value > target) {
      right--;
    } else {
      left++;
    }
  }
};

const value = twoSum([2, 7, 11, 15], 9);
const value2 = twoSum([2, 3, 4], 6);
const value3 = twoSum([-1, 0], -1);
const value4 = twoSum([0, 0, 3, 4], 0);
console.log(value); // [0, 1]
console.log(value2); // [0, 2]
console.log(value3); // [0, 1]
console.log(value4); // [0, 1]
