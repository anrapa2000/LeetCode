var containsDuplicate = function(nums) {
    values = new Set(nums);
    return values.size !== nums.length;
};

console.log(containsDuplicate([1,2,3,1]))