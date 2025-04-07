from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefixSum = [0] * len(nums)
        # suffixSum = [0] * len(nums)
        # result = [0] * len(nums)
        # prefixSum[0] = 1
        # for i in range(1, len(nums)):
        #     prefixSum[i] = prefixSum[i - 1] * nums[i - 1]

        # suffixSum[len(nums) - 1] = 1
        # for i in range(len(nums) - 2, -1, -1):
        #     suffixSum[i] = suffixSum[i + 1] * nums[i + 1]

        # for i in range(0, len(nums)):
        #     result[i] = prefixSum[i] * suffixSum[i]
        # return result

        # length = len(nums)
        # prefixSum = [0] * length
        # suffixSum = [0] * length
        # prefixSum[0] = 1
        # result = [0] * length

        # for i in range(1, length):
        #     prefixSum[i] = prefixSum[i - 1] * nums[i - 1]

        # suffixSum[length - 1] = 1
        # for i in range(length - 2, -1, -1):
        #     suffixSum[i] = suffixSum[i + 1] * nums[i + 1]

        # for i in range(length):
        #     result[i] = prefixSum[i] * suffixSum[i]
        # return result
        length = len(nums)
        result = [1] * length
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result


value = Solution().productExceptSelf([1, 2, 3, 4])
print(value)
