from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [0] * len(nums)
        suffixSum = [0] * len(nums)
        result = [0] * len(nums)
        prefixSum[0] = 1
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] * nums[i - 1]

        suffixSum[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] * nums[i + 1]

        for i in range(0, len(nums)):
            result[i] = prefixSum[i] * suffixSum[i]
        return result


value = Solution().productExceptSelf([1, 2, 3, 4])
print(value)
