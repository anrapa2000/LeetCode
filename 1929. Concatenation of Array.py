from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        print(length)
        array = [0] * length * 2
        for i in range(len(nums)):
            array[i] = nums[i]
            array[i + length] = nums[i]
        return array


print(Solution().getConcatenation([1, 2, 3, 1]))
