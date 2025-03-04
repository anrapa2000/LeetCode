/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let max = 0;
    let i = 0;
    let k = height.length - 1;
    while(i < k){
        let area = Math.min(height[i], height[k]) * (k - i);
        max = Math.max(max, area);
        if(height[i] < height[k]){
            i++;
        }
        else{
            k--;
        }
    }
    return max;
};

console.log(maxArea([1,8,6,2,5,4,8,3,7])); // 49
console.log(maxArea([1,1])); // 1