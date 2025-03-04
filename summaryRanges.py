from typing import List


class Solution:
    def summaryRanges(self, nums) -> List[str]:
        i = 0
        array = []
        string = ""
        start = nums[0]
        while(nums[i] + 1 == nums[i+1]):
            i = i + 1
        end = nums[i]
        print(str(start), "->", str(end))








value = Solution()
print(value.summaryRanges([0,1,2,4,5,7]))
print(value.summaryRanges([0,2,3,4,6,8,9]))
print(value.summaryRanges([]))