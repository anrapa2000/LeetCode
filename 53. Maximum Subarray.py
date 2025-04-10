from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxVal = currentVal = nums[0]
        # for num in nums[1:]:
        #     currentVal = max(num, num + currentVal)
        #     maxVal = max(currentVal, maxVal)
        # return maxVal

        # maxVal = nums[0]
        # currentVal = 0
        # for num in nums:
        #     if currentVal < 0:
        #         currentVal = 0
        #     currentVal += num
        #     maxVal = max(currentVal, maxVal)
        # return maxVal

        currentMax = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            if num < currentMax + num:
                currentMax += num
            else:
                currentMax = num

            if currentMax > maxSum:
                maxSum = currentMax
        return maxSum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([-2, 1]))
print(Solution().maxSubArray([-1]))
