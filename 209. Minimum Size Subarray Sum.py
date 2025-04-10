class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        sum = 0
        minLength = float("inf")
        for right in range(0, len(nums)):
            sum += nums[right]
            while sum >= target:
                sum -= nums[left]
                minLength = min(minLength, right - left + 1)
                left += 1
        return minLength if minLength > 0 else 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
